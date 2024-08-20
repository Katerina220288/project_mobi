import By
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import requests
from selenium.webdriver.support import expected_conditions as EC


link= ("https://www.automotiveannotation.com/")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

browser.get(link)
time.sleep(2)
contact_button=browser.find_element(By.XPATH,'//*[@id="menu-item-1238"]/a')
time.sleep(3)
contact_button.click()
name_input=browser.find_element(By.XPATH,'//*[@id="wpcf7-f1169-p14-o1"]/form/label[1]/span/input')
time.sleep(2)
name_input.send_keys("Auto_test")
time.sleep(2)
email_input=browser.find_element(By.XPATH,'//*[@id="wpcf7-f1169-p14-o1"]/form/label[2]/span/input')
time.sleep(2)
email_input.send_keys("qa@qa.com")
time.sleep(2)
body_input=browser.find_element(By.XPATH,'//*[@id="wpcf7-f1169-p14-o1"]/form/label[3]/span/textarea')
time.sleep(3)
body_input.send_keys("qainhouseteam")
time.sleep(3)
button=browser.find_element(By.XPATH,'//*[@id="wpcf7-f1169-p14-o1"]/form/input')
time.sleep(3)
button.click()
time.sleep(3)
#try:
   # element = WebDriverWait(browser, 10).until(
       # EC.presence_of_element_located((By.XPATH, '//*[@id="wpcf7-f1169-p14-o1"]/form/div[2]'))
# print("Element is visible!")
response_element =browser.find_element(By.XPATH, '//*[@id="wpcf7-f1169-p14-o1"]/form/div[2]')
if response_element.is_displayed():
    print("Thank you for your message!")
else:
    print("Error: Element not found or not visible")

upload_file = webdriver.find_element(By.XPATH,
                                     upload_file.send.keys