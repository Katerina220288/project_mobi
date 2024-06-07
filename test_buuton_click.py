from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class HeaderButtonsTest(unittest.TestCase):

    def setUp(self):
        # Вказуємо шлях до вебдрайвера (наприклад, для Chrome)
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.hireiotdevelopers.com/')  # Замінимо на URL вашого сайту

    def test_buttons(self):
        driver = self.driver

        # Список кнопок для перевірки
        buttons = {
            "Contact us": "/html/body/header/div/div/div[2]/a",
            "Blog": "/html/body/header/div/div/div[1]/a[5]",
            "Home": "/html/body/header/div/div/div[1]/a[1]",
            "Why us": "/html/body/header/div/div/div[1]/a[2]",
            "Expertise": "/html/body/header/div/div/div[1]/a[3]",
            "Services": "/html/body/header/div/div/div[1]/a[4]"
        }

        for button_name, xpath in buttons.items():
            try:
                # Перевіряємо наявність кнопки
                button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                print(f"{button_name} button is present.")

                # Перевіряємо клікабельність кнопки
                clickable = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                if clickable.is_enabled():
                    print(f"{button_name} button is clickable.")
                else:
                    print(f"{button_name} button is not clickable.")
            except Exception as e:
                print(f"Error with {button_name} button: {e}")

        def tearDown(self):
            self.driver.quit()

    if __name__ == "__main__":
        unittest.main()