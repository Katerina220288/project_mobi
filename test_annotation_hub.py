from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

link= ("https://annotation-hub.com/")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()
browser.get(link)
time.sleep(2)
button=browser.find_element(By.XPATH,'//*[@id="menu-item-325"]/a')
time.sleep(3)
button.click()
time.sleep(3)
name_input=browser.find_element(By.XPATH,'//*[@id="wpcf7-f2376-p305-o1"]/form/div[2]/div[1]/span/input')
time.sleep(2)
name_input.send_keys("Auto_test")
time.sleep(2)
last_name_input=browser.find_element(By.XPATH,'//*[@id="wpcf7-f2376-p305-o1"]/form/div[2]/div[2]/span/input')
time.sleep(2)
name_input.send_keys("test")
time.sleep(2)
email_input=browser.find_element(By.XPATH,'//*[@id="wpcf7-f2376-p305-o1"]/form/div[2]/div[3]/span/input')
time.sleep(2)
email_input.send_keys("qa@qa.com")
time.sleep(2)
body_input=browser.find_element(By.XPATH,'//*[@id="wpcf7-f2376-p305-o1"]/form/div[2]/div[4]/span/textarea')
time.sleep(3)
body_input.send_keys("no need to answer")
time.sleep(3)

button=browser.find_element(By.XPATH,'//*[@id="wpcf7-f29-p8-o1"]/form/input')
time.sleep(3)
button.click()
time.sleep(3)