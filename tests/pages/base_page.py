from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Общие локаторы
    search_input_field = (By.XPATH, "//input[@id='searchInput']")

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait_for_element(locator).click()

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        return self.wait_for_element(locator).text

    def refresh_page(self):
        self.driver.refresh()

    @staticmethod
    def assert_is_empty(element):
        """Check if the input field is empty."""
        value = element.get_attribute("value")  # Correctly fetch the value attribute
        assert value == "", f"Field is not empty! Current value: '{value}'"



