from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

link= ("https://www.saucedemo.com/")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()
browser.get(link)
time.sleep(2)

Username_input=browser.find_element(By.XPATH,'//*[@id="user-name"]')
time.sleep(2)
Username_input.send_keys("standard_user")
time.sleep(2)
Password_input=browser.find_element(By.XPATH,'//*[@id="password"]')
time.sleep(2)
Password_input.send_keys("secret_sauce")
time.sleep(2)

Login_button=browser.find_element(By.XPATH,'//*[@id="login-button"]')
time.sleep(3)
Login_button.click()
time.sleep(3)

browser.quit()
