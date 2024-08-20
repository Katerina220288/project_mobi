from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_sauce_demo_login():
    try:
        link = "https://www.saucedemo.com/"
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(options=options)
        browser.get(link)
        time.sleep(2)

        try:
            username_input = browser.find_element(By.XPATH, '//*[@id="user-name"]')
            username_input.send_keys("standard_user")

            password_input = browser.find_element(By.XPATH, '//*[@id="password"]')
            password_input.send_keys("secret_sauce")

            login_button = browser.find_element(By.XPATH, '//*[@id="login-button"]')
            login_button.click()
            time.sleep(2)
        except Exception as e:
            print(f"Error finding or elements: {e}")
            return

        
        if "inventory.html" in browser.current_url:
            print("Login successful.")
        else:
            print("Login failed.")
    except Exception as e:
        print(f"Error initializing the browser or opening the website: {e}")
    finally:
        try:
            browser.quit()
        except Exception as e:
            print(f"Error quitting the browser: {e}")

if __name__ == "__main__":
    test_sauce_demo_login()