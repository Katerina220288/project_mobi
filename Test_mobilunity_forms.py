import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Fixture for WebDriver setup and teardown
@pytest.fixture(scope="module")
def driver():
    driver_path = 'path/to/your/webdriver'
    driver = webdriver.Chrome(executable_path=driver_path)
    yield driver
    driver.quit()


# Helper function to get an element
def get_element(driver, locator):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(locator)
    )


# Test data
websites = [
    'https://mobilunity.co.il/',
    'https://mobilunity.nl/',
    'https://mobilunity.dk/',
    'https://mobilunity.de/',

]
First_name = 'Test User'
Last_name = 'Ilnicka'
email = 'qa@qa.com'
body = 'This is a test message.'
file_path = '/path/to/your/testfile.txt'


# Test function
@pytest.mark.parametrize("website", websites)
def test_form_submission(driver, website):
    driver.get(website)

    try:
        # Locate and fill out the Name field
        name_field = get_element(driver, (By.NAME, "name"))
        name_field.send_keys(name)

        # Locate and fill out the Email field
        email_field = get_element(driver, (By.NAME, "email"))
        email_field.send_keys(email)

        # Locate and fill out the Body field
        body_field = get_element(driver, (By.NAME, "body"))
        body_field.send_keys(body)

        # Locate and attach a file
        attach_file_field = get_element(driver, (By.NAME, "file"))
        attach_file_field.send_keys(file_path)

        # Locate and click the Submit button
        submit_button = get_element(driver, (By.NAME, "submit"))
        submit_button.click()

        # Wait for the form to be submitted and a response to be loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Example assertion: Check for a success message
        success_message = driver.find_elements(By.XPATH, "//*[contains(text(), 'success')]")
        assert success_message, f"Form submission failed for {website}. Success message not found."

        print(f"Form submitted successfully for {website}")

    except Exception as e:
        print(f"An error occurred on {website}: {e}")
        pytest.fail(f"Test failed on {website} due to {e}")


# Run the test
if __name__ == "__main__":
    pytest.main(["-s", __file__])
