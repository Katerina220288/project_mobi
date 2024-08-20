from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


def run_test():

    # Встановлення драйвера для браузера
 driver = webdriver.Chrome()

 try:
    # Відкриття веб-сторінки з випадаючим меню
    driver.get('https://www.sf-recruiters.com/')

    # Очікування кнопки меню та клік на неї для відкриття випадаючого списку
    menu_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="menu-item-2322"]'))
    )

    # Наведення мишкою на кнопку для відображення випадаючого списку
    actions = ActionChains(driver)
    actions.move_to_element(menu_button).perform()

    # Очікування появи випадаючого меню та клік на один з елементів
    dropdown_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-1613"]'))
    )
    dropdown_item.click()

    # Очікування завантаження нової сторінки та перевірка URL
    new_url = 'https://www.sf-recruiters.com/case-studies/'
    WebDriverWait(driver, 10).until(
        EC.url_to_be(new_url)
    )
    confirmation_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, '/html/body/div[3]/div[1]/div/div[1]/div/div/h1'))
    )
        # Якщо URL відповідає очікуваному, тест успішний
    if driver.current_url == new_url and confirmation_element.is_displayed():
        print('Тест пройшов успішно: Нова сторінка відкрилася і елемент знайдено')

 except Exception as e:
      print(f'Тест не пройшов: Невідома помилка - {e}')
 except NoSuchElementException as e:
      print(f'Тест не пройшов: Елемент не знайдено - {e}')
 
  finally:
    # Закриття драйвера
    driver.quit()

if __name__ == "__main__":
    run_test()
