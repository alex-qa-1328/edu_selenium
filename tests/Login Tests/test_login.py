import time
import pytest
from selenium.webdriver.common.by import By
from tests.pages.login_page import LoginPage


@pytest.mark.login
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login()
    actual_username = driver.find_element(By.XPATH, "//*[@id='pt-userpage']/a/span").text.lower()

    # time.sleep(5)
    assert LoginPage.username in actual_username, f"Expected username '{LoginPage.username}' to be in '{actual_username}'"
    print(f"Проверка что введеное имя пользователя: {LoginPage.username}\nсовпадает с указанным на сайте после входа: {actual_username}")


