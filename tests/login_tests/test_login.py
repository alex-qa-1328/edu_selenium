import pytest
from selenium.webdriver.common.by import By

from tests.pages import login_page
from tests.pages.base_page import BasePage
from tests.pages.login_page import LoginPage
# from tests.conftest import driver


@pytest.mark.login
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(LoginPage.valid_username, LoginPage.valid_password)
    actual_username = driver.find_element(By.XPATH, "//*[@id='pt-userpage']/a/span").text.lower()
    # actual_username = "thetestuser13934923"

    assert LoginPage.valid_username in actual_username, f"Expected username '{LoginPage.valid_username}' to be in '{actual_username}'"
    print(f"Проверка что введеное имя пользователя: {LoginPage.valid_username}\nсовпадает с указанным на сайте после входа: {actual_username}")

@pytest.mark.negative
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



@pytest.mark.parametrize("login", LoginPage.login_data())
def test_login_input_validation(driver, login):
    login_url = "https://ru.wikipedia.org/w/index.php?returnto=%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F+%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0&title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%92%D1%85%D0%BE%D0%B4&centralAuthAutologinTried=1&centralAuthError=Not+centrally+logged+in"
    base_page = BasePage(driver)
    driver.get(login_url)
    print(f"Открываем страницу авторизации: {login_url}")

    BasePage.assert_is_empty(driver.find_element(*LoginPage.username_input))
    print("Проверяем что поле логин пустое")

    driver.find_element(*LoginPage.username_input).send_keys(login)
    print(f"Вводим значение: {login}")

    assert driver.find_element(*LoginPage.username_input).get_attribute("value") == login
    print(f"Проверяем, что в поле логин отображается введеный нами логин\nОжидаем: {login}\nФактически:{driver.find_element(*LoginPage.username_input).get_attribute("value")}")

    base_page.refresh_page()
    print("Обновляем страницу")

    BasePage.assert_is_empty(driver.find_element(*LoginPage.username_input))
    print("Проверяем, что поле логин снова пустое")
