from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
from twocaptcha import TwoCaptcha

# Параметри для вирішення капчі
API_KEY = '3061c419f89285010ad583ff2d1c1849'
site_key = 'af0bced3-7d4f-40ff-bded-8511552f97d1'
url = 'https://www.bestiotjobs.com/contact-us/'
SECRET_KEY = 'ES_25c0b936160949cf99ecd022156185d8'

def solve_captcha():
    # Відправка запиту на вирішення капчі
    response = requests.post('http://2captcha.com/in.php', data={
        'key': API_KEY,
        'method': 'hcaptcha',
        'sitekey': site_key,
        'pageurl': url
    })

    if response.status_code != 200 or response.text[0:2] != 'OK':
        print('Error sending captcha solving request')
        print(response.text)
        return None
    else:
        captcha_id = response.text.split('|')[1]
        print(f'Captcha ID: {captcha_id}')

        # Отримання результату
        while True:
            time.sleep(5)  # Зачекайте кілька секунд перед перевіркою результату
            result_response = requests.get(f'http://2captcha.com/res.php?key={API_KEY}&action=get&id={captcha_id}')

            if result_response.text == 'CAPCHA_NOT_READY':
                continue
            elif result_response.text[0:2] == 'OK':
                captcha_code = result_response.text.split('|')[1]
                print('Captcha solved: ' + captcha_code)

                # Перевірка відповіді капчі за допомогою секретного ключа hCaptcha
                verification_response = requests.post('https://hcaptcha.com/siteverify', data={
                    'secret': SECRET_KEY,
                    'response': captcha_code
                })
                verification_result = verification_response.json()

                if verification_result['success']:
                    print('Captcha successfully verified')
                    return captcha_code
                else:
                    print('Captcha verification failed')
                    print(verification_result)
                    return None
            else:
                print('Error retrieving captcha result')
                print(result_response.text)
                return None

# URL форми та заповнення форми
link = "https://www.bestiotjobs.com/contact-us/"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(browser, 3)
browser.get(link)
time.sleep(2)

# Заповнення форми
name_input = browser.find_element(By.XPATH, '//*[@id="wpcf7-f4686-p4707-o1"]/form/p[1]/label/span/input')
time.sleep(2)
name_input.send_keys("Auto_test with captcha")
time.sleep(2)
email_input = browser.find_element(By.XPATH, '//*[@id="wpcf7-f4686-p4707-o1"]/form/p[2]/label[1]/span/input')
time.sleep(2)
email_input.send_keys("qa@qa.com")
time.sleep(2)
subject_input = browser.find_element(By.XPATH, '//*[@id="wpcf7-f4686-p4707-o1"]/form/p[2]/label[3]/span/input')
time.sleep(3)
subject_input.send_keys("qainhouseteam")
time.sleep(5)
body_input = browser.find_element(By.XPATH, '//*[@id="wpcf7-f4686-p4707-o1"]/form/p[3]/label/span/textarea')
time.sleep(3)
body_input.send_keys("no need to answer")
time.sleep(3)

captcha_code = solve_captcha()

if captcha_code:
    # Введення капчі в поле, якщо таке існує
    try:
        # Зачекаємо появи капчі
        # Set the solved Captcha

        #recaptcha_response_element = browser.find_element(By.XPATH, '//textarea[contains(@id,"h-captcha-response")]')
        recaptcha_response_element = wait.until(
            EC.presence_of_element_located((By.XPATH, '//textarea[contains(@id,"h-captcha-response")]')))
       # field = browser.find_element(By.XPATH, '//textarea[contains(@style.display = ;")]')
        #recaptcha_response_element = browser.find_element(By.ID, '{captcha_id}')
        #browser.execute_script("arguments[0].style.display = 'block'; arguments[0].style.visibility = 'visible';",
                              # recaptcha_response_element)   # Зробимо елемент видимим
        #wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[contains(@id="h-captcha-response")]')))
        browser.execute_script(f"document.querySelector('[name=\"h-captcha-response\"]').innerHTML='{captcha_code}'")
        browser.execute_script(f'arguments[0].value = "{captcha_code}";', recaptcha_response_element)
        time.sleep(5)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wpcf7-f4686-p4707-o1"]/form/p[4]/input')))
        button.click()


    except Exception as e:

        print(f"Failed to solve captcha. Error: {e}")

    else:

        print("Failed to obtain captcha code.")



