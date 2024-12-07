import pytest
from selenium.webdriver.common.by import By
from tests.pages.login_page import LoginPage


@pytest.mark.login
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(LoginPage.valid_username, LoginPage.valid_password)
    actual_username = driver.find_element(By.XPATH, "//*[@id='pt-userpage']/a/span").text.lower()
    # actual_username = "thetestuser13934923"

    assert LoginPage.valid_username in actual_username, f"Expected username '{LoginPage.valid_username}' to be in '{actual_username}'"
    print(f"Проверка что введеное имя пользователя: {LoginPage.valid_username}\nсовпадает с указанным на сайте после входа: {actual_username}")

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(LoginPage.invalid_username, LoginPage.invalid_password)

    # error_message = driver.find_element(LoginPage.error_message)
    error_message = login_page.get_error_message()
    print(f"\nНаходим сообщение об ошибке:\n{error_message}")
    expected_error_1 = "Введены неверные имя участника или пароль. Попробуйте ещё раз."
    expected_error_2 = "Возникли проблемы с отправленными данными"

    assert error_message in expected_error_1 or error_message in expected_error_2
    print(f"\nПроверяем, что сообщение об ошибке совпадает с ожидаемой:\n{expected_error_1}\nили\n{expected_error_2}")


