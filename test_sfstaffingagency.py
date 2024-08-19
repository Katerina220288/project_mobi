from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

link= ("https://www.sfstaffingagency.com/")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()
browser.get(link)

button=browser.find_element(By.XPATH,'//*[@id="menu-item-405"]/a')
time.sleep(3)
name_input=browser.find_element(By.XPATH,'//*[@id="wpcf7-f6-p358-o1"]/form/label[1]/span/input')
time.sleep(2)
name_input.send_keys("Auto_test")
time.sleep(2)
email_input=browser.find_element(By.XPATH,'//*[@id="wpcf7-f6-p358-o1"]/form/label[2]/span/input')
time.sleep(2)
email_input.send_keys("qa@qa.com")
time.sleep(2)
subject_input=browser.find_element(By.XPATH,'//*[@id="wpcf7-f6-p358-o1"]/form/label[3]/span/input')
time.sleep(3)
subject_input.send_keys("qainhouseteam")
time.sleep(2)
body_input=browser.find_element(By.XPATH,'//*[@id="wpcf7-f6-p358-o1"]/form/label[4]/span/textarea')
time.sleep(3)
body_input.send_keys("no need to answer")
time.sleep(3)
button=browser.find_element(By.XPATH,'//*[@id="wpcf7-f6-p358-o1"]/form/input')
time.sleep(3)
button.click()
time.sleep(3)
browser.quit()
status: str = 'email_sent'
if (status:='email_sent'):
    print("Thank you")
else:
    print('Error')

