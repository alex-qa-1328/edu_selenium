from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
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
        value = element.get_attribute("value")
        assert value == "", f"Поле не пустое! Его значение: '{value}'"

    # @staticmethod
    def double_click(self, element):
        if not isinstance(self.driver, WebDriver):
            raise ValueError("Invalid WebDriver instance passed to ActionChains.")

        action = ActionChains(self.driver)
        action.double_click(element).perform()
        print(f"Двойной клик на элемент: {element}")

    def right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element).perform()
        print(f"Нажатие правой кнопки мыши на элемент: {element}")




