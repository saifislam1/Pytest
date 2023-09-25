import subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class TestSauceDemo:

    # Class-level WebDriver instance
    driver = webdriver.Chrome()

    # Locators
    USERNAME_LOCATOR = (By.CSS_SELECTOR, '#user-name')
    PASSWORD_LOCATOR = (By.CSS_SELECTOR, '#password')
    SUBMIT_LOCATOR = (By.CSS_SELECTOR, '.btn_action')

    def setup_class(cls):
        # Navigate to the SauceDemo site once for the entire test class
        cls.driver.get('http://www.saucedemo.com/v1')

    def teardown_class(cls):
        # Close the WebDriver instance once all tests in the class have run
        cls.driver.quit()

    def test_valid_credentials_login(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(self.USERNAME_LOCATOR))
        username_element = driver.find_element(*self.USERNAME_LOCATOR)
        password_element = driver.find_element(*self.PASSWORD_LOCATOR)
        submit_element = driver.find_element(*self.SUBMIT_LOCATOR)
        username_element.send_keys('standard_user')
        password_element.send_keys('secret_sauce')
        submit_element.click()
        assert "/inventory.html" in driver.current_url
