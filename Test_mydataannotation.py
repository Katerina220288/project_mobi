from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

link= ("https://www.mydataannotation.com/#contact")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()
browser.get(link)
time.sleep(2)
name_input=browser.find_element(By.XPATH,'//*[@id="wpcf7-f55-p33-o1"]/form/p[1]/label/span/input')
time.sleep(2)
name_input.send_keys("Auto_test")
time.sleep(2)
email_input=browser.find_element(By.XPATH,'//*[@id="wpcf7-f55-p33-o1"]/form/p[2]/label[1]/span/input')
time.sleep(2)
email_input.send_keys("qa@qa.com")
time.sleep(2)
subject_input=browser.find_element(By.XPATH,'//*[@id="wpcf7-f55-p33-o1"]/form/p[2]/label[2]/span/input')
time.sleep(3)
subject_input.send_keys("qainhouseteam")
time.sleep(5)
body_input=browser.find_element(By.XPATH,'//*[@id="wpcf7-f55-p33-o1"]/form/p[2]/label[3]/span/textarea')
time.sleep(3)
body_input.send_keys("no need to answer")
time.sleep(3)
button=browser.find_element(By.XPATH,'//*[@id="wpcf7-f55-p33-o1"]/form/p[3]/input')
time.sleep(3)
button.click()
time.sleep(3)
status: str = 'email_sent'
if (status:='email_sent'):
    print("Thank you")
else:
    print('Error')
browser.quit()
