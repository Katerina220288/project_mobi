from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time




link = "https://www.bestiotjobs.com/contact-us/"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(browser, 3)
captcha_code = "123456asd"
browser.get(link)
time.sleep(2)
try:
    # Зачекаємо появи капчі
    # Set the solved Captcha

    recaptcha_response_element_input = browser.find_element(By.XPATH, '//textarea[contains(@id,"h-captcha-response")]')
    #browser.execute_script("arguments[0].style.display = 'block'; arguments[0].style.visibility = 'visible';",
                           #recaptcha_response_element_input)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[contains(@id="h-captcha-response")]')))
    #browser.execute_script(f'arguments[0].value = "{captcha_code}"; arguments[0].dispatchEvent(new Event("input", {{ bubbles: true }}));', recaptcha_response_element)
    #recaptcha_response_element.send_keys(captcha_code)
    #browser.execute_script("arguments[0].value = '{captcha_code}';", recaptcha_response_element_input)
    #browser.execute_script(recaptcha_response_element_input, captcha_code)

    #browser.execute_script(f'arguments[0].value = "{captcha_code}";',  recaptcha_response_element_input)
    browser.execute_script(f'arguments[0].value = "{captcha_code}";', recaptcha_response_element_input)
    browser.execute_script(f"document.querySelector('[name=\"h-captcha-response\"]').innerHTML='{captcha_code}'")
    assert recaptcha_response_element_input.get_property('value') == captcha_code, "captcha code wasn't set"


    # Перевірити, що значення вставлено
    inserted_value = browser.execute_script('return arguments[0].value;', recaptcha_response_element_input)
    assert inserted_value == captcha_code, "Captcha code was not inserted correctly"

except:
    print("Failed to solve captcha.")
    time.sleep(5)
    browser.close()