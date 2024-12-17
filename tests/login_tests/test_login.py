import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.pages.base_page import BasePage
from tests.pages.login_page import LoginPage


@pytest.mark.login
def test_valid_login(driver, login_page):
    login_page.login(LoginPage.valid_username, LoginPage.valid_password)
    actual_username = driver.find_element(By.XPATH, "//*[@id='pt-userpage']/a/span").text.lower()
    # actual_username = "2323thetestuser13534923"

    assert LoginPage.valid_username in actual_username, f"Expected username '{LoginPage.valid_username}' to be in '{actual_username}'"
    print(f"Проверка что введеное имя пользователя: {LoginPage.valid_username}\nсовпадает с указанным на сайте после входа: {actual_username}")

@pytest.mark.negative
def test_invalid_login(driver, login_page):
    login_page.login(LoginPage.invalid_username, LoginPage.invalid_password)
    expected_url = "https://ru.wikipedia.org/w/index.php?title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%92%D1%85%D0%BE%D0%B4&returnto=%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F+%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
    unexpected_url = "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
    error_message = login_page.get_error_message()
    print(f"\nНаходим сообщение об ошибке:\n{error_message}")

    expected_error_1 = "Введены неверные имя участника или пароль. Попробуйте ещё раз."
    expected_error_2 = "Возникли проблемы с отправленными данными"

    assert error_message == expected_error_1 or error_message == expected_error_2
    print(f"\nПроверяем, что сообщение об ошибке совпадает с ожидаемой:\n{expected_error_1}\nили\n{expected_error_2}")

    assert driver.current_url == expected_url, "Ожидаемый и фактический URL не совпадают!"
    print(f"Ожидаемый URL:\n{expected_url}\nФактический URL:\n{driver.current_url}")

    # assert driver.current_url != unexpected_url, "Неожидаемый и фактический URL совпадают!"
    # print(f"НЕожидаемый URL:\n{unexpected_url}\nФактический URL:\n{driver.current_url}")

@pytest.mark.parametrize("login", LoginPage.login_data())
def test_login_input_validation(driver, login, base_page, login_page):
    driver.get(login_page.login_url)
    print(f"Открываем страницу авторизации: {login_page.login_url}")

    BasePage.assert_is_empty(driver.find_element(*login_page.username_input))
    print("Проверяем что поле логин пустое")

    driver.find_element(*login_page.username_input).send_keys(login)
    print(f"Вводим значение: {login}")

    assert driver.find_element(*login_page.username_input).get_attribute("value") == login
    print(f"Проверяем, что в поле логин отображается введеный нами логин\nОжидаем: {login}\nФактически:{driver.find_element(*LoginPage.username_input).get_attribute("value")}")

    base_page.refresh_page()
    print("Обновляем страницу")

    base_page.assert_is_empty(driver.find_element(*login_page.username_input))
    print("Проверяем, что поле логин снова пустое")

def test_key_enter(driver, base_page, login_page):
    old_expected_url = "https://ru.wikipedia.org/wiki/%D0%A6%D0%B8%D1%86%D0%B5%D1%80%D0%BE%D0%BD"
    expected_url = "https://ru.wikipedia.org/w/index.php?fulltext=%D0%9D%D0%B0%D0%B9%D1%82%D0%B8&search=%D0%A6%D0%B8%D1%86%D0%B5%D1%80%D0%BE%D0%BD&title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F%3A%D0%9F%D0%BE%D0%B8%D1%81%D0%BA&ns0=1"

    driver.get(login_page.main_page_url)
    print(f"Открываем главную страницу Википедии:\n{login_page.main_page_url}")

    driver.find_element(*base_page.search_input_field).send_keys("Цицерон")
    print("Вводим в поисковую строку: Цицерон")

    driver.find_element(*base_page.search_input_field).send_keys(Keys.ENTER)
    # driver.find_element(*base_page.search_input_field).send_keys(Keys.TAB * 5)
    print("Нажимаем кнопку Enter")

    assert driver.current_url == expected_url
    # assert driver.current_url != old_expected_url
    print(f"Проверяем что фактический URL:\n{driver.current_url}\nсовпадает с ожидаемым:\n{expected_url}")


def test_always_fails(driver):
    driver.get("https://ru.wikipedia.org/wiki/%D0%A6%D0%B8%D1%86%D0%B5%D1%80%D0%BE%D0%BD")
    assert driver.title == "ASDJHALSKJDHIUHkJSHDJNSDKJHKSHDKSHD"  # Тест гарантировано упадет


