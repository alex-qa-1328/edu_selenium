from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage


class Web_Elements(BasePage):

    web_el_url = "https://demoqa.com/buttons"

    # Локаторы:
    double_click_button = By.ID, "doubleClickBtn"
    right_click_button = (By.ID, "rightClickBtn")
    double_click_message = (By.ID, "doubleClickMessage")
    right_click_message = (By.ID, "rightClickMessage")

    plus_button = (By.XPATH, "//button[@title='Expand all']")
    minus_button = (By.XPATH, "//button[@title='Collapse all']")