from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

# Параметри для вирішення капчі
API_KEY = '3061c419f89285010ad583ff2d1c1849'
site_key = 'af0bced3-7d4f-40ff-bded-8511552f97d1'
url = 'https://www.bestiotjobs.com/contact-us/'
SECRET_KEY = 'ES_25c0b936160949cf99ecd022156185d8'

# Instantiate the WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Load the target page
driver.get(url)
time.sleep(2)

# Заповнення форми
name_input = driver.find_element(By.XPATH, '//*[@id="wpcf7-f4686-p4707-o1"]/form/p[1]/label/span/input')
time.sleep(2)
name_input.send_keys("Auto_test with captcha")
time.sleep(2)
email_input = driver.find_element(By.XPATH, '//*[@id="wpcf7-f4686-p4707-o1"]/form/p[2]/label[1]/span/input')
time.sleep(2)
email_input.send_keys("qa@qa.com")
time.sleep(2)
subject_input = driver.find_element(By.XPATH, '//*[@id="wpcf7-f4686-p4707-o1"]/form/p[2]/label[3]/span/input')
time.sleep(3)
subject_input.send_keys("qainhouseteam")
time.sleep(5)
body_input = driver.find_element(By.XPATH, '//*[@id="wpcf7-f4686-p4707-o1"]/form/p[3]/label/span/textarea')
time.sleep(3)
body_input.send_keys("no need to answer")
time.sleep(3)

# Натискання кнопки для виклику капчі
button = driver.find_element(By.XPATH, '//*[@id="wpcf7-f4686-p4707-o1"]/form/p[4]/input')
time.sleep(3)
button.click()

# Solve the Captcha
print("Solving Captcha")
solver = TwoCaptcha('3061c419f89285010ad583ff2d1c1849')
response = solver.hcaptcha(sitekey=site_key, url=url)
code = response['code']
print(f"Successfully solved the Captcha. The solve code is {code}")

# Set the solved Captcha
recaptcha_response_element = driver.find_element(By.XPATH, '//*[@id="h-captcha-response-03i4ix5d9rqe"]')
driver.execute_script("arguments[0].style.display = 'block';", recaptcha_response_element)  # Зробимо елемент видимим
driver.execute_script(f'arguments[0].value = "{code}";', recaptcha_response_element)

# Submit the form
submit_btn = driver.find_element(By.XPATH, '//*[@id="wpcf7-f4686-p4707-o1"]/form/p[4]/input')
time.sleep(3)
submit_btn.click()

# Pause the execution so you can see the screen after submission before closing the driver
input("Press enter to continue")
driver.close()







