import subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from colorama import init, Fore, Back

# Initialize colorama for color output
init(autoreset=True)

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

        # Explicitly wait for the username field to be displayed
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME_LOCATOR)
        )

        # Find elements
        username_element = driver.find_element(*self.USERNAME_LOCATOR)
        password_element = driver.find_element(*self.PASSWORD_LOCATOR)
        submit_element = driver.find_element(*self.SUBMIT_LOCATOR)

        # Input credentials and submit
        username_element.send_keys('standard_user')
        password_element.send_keys('secret_sauce')
        submit_element.click()

        # Assertion
        assert "/inventory.html" in driver.current_url

    def test_run_jmeter(self):
        test_plan_path = "C:/Users/shaju/OneDrive/Desktop/Software/apache-jmeter-5.6.2/bin/templates/functional-testing-01-test-plan.jmx"
        jmeter_path = "C:/Users/shaju/OneDrive/Desktop/Software/apache-jmeter-5.6.2/bin/jmeter.bat"  # Path to JMeter executable

        with subprocess.Popen([jmeter_path, "-n", "-t", test_plan_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
            for line in proc.stdout:
                if "WARN" in line:
                    print(Fore.YELLOW + line, end='')  # Yellow for warnings
                elif "Err:" in line and "100.00%" in line:
                    print(Fore.RED + line, end='')  # Red for errors
                else:
                    print(line, end='')  # Default color for other lines
            stdout, stderr = proc.communicate()

        # Here, you can include any additional processing or checks for the JMeter output, if needed.

# If you want to run the test manually via this script (outside of pytest)
if __name__ == "__main__":
    tests = TestSauceDemo()
    tests.setup_class()
    try:
        tests.test_valid_credentials_login()
        tests.test_run_jmeter()  # Execute JMeter after the Selenium test
    finally:
        tests.teardown_class()
