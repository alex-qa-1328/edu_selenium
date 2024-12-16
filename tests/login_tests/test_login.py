import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.pages.base_page import BasePage
from tests.pages.login_page import LoginPage


@pytest.mark.login
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(LoginPage.valid_username, LoginPage.valid_password)
    actual_username = driver.find_element(By.XPATH, "//*[@id='pt-userpage']/a/span").text.lower()
    # actual_username = "2323thetestuser13534923"

    assert LoginPage.valid_username in actual_username, f"Expected username '{LoginPage.valid_username}' to be in '{actual_username}'"
    print(f"Проверка что введеное имя пользователя: {LoginPage.valid_username}\nсовпадает с указанным на сайте после входа: {actual_username}")

@pytest.mark.negative
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login(LoginPage.invalid_username, LoginPage.invalid_password)

    error_message = login_page.get_error_message()
    print(f"\nНаходим сообщение об ошибке:\n{error_message}")

    expected_error_1 = "Введены неверные имя участника или пароль. Попробуйте ещё раз."
    expected_error_2 = "Возникли проблемы с отправленными данными"

    assert error_message == expected_error_1 or error_message == expected_error_2
    print(f"\nПроверяем, что сообщение об ошибке совпадает с ожидаемой:\n{expected_error_1}\nили\n{expected_error_2}")

@pytest.mark.parametrize("login", LoginPage.login_data())
def test_login_input_validation(driver, login):
    base_page = BasePage(driver)
    driver.get(LoginPage.login_url)
    print(f"Открываем страницу авторизации: {LoginPage.login_url}")

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

def test_key_enter(driver):
    old_expected_url = "https://ru.wikipedia.org/wiki/%D0%A6%D0%B8%D1%86%D0%B5%D1%80%D0%BE%D0%BD"
    expected_url = "https://ru.wikipedia.org/w/index.php?fulltext=%D0%9D%D0%B0%D0%B9%D1%82%D0%B8&search=%D0%A6%D0%B8%D1%86%D0%B5%D1%80%D0%BE%D0%BD&title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F%3A%D0%9F%D0%BE%D0%B8%D1%81%D0%BA&ns0=1"

    driver.get(LoginPage.main_page_url)
    print(f"Открываем главную страницу Википедии:\n{LoginPage.main_page_url}")

    driver.find_element(*BasePage.search_input_field).send_keys("Цицерон")
    print("Вводим в поисковую строку: Цицерон")

    driver.find_element(*BasePage.search_input_field).send_keys(Keys.ENTER)
    # driver.find_element(*BasePage.search_input_field).send_keys(Keys.TAB * 5)
    print("Нажимаем кнопку Enter")

    assert driver.current_url == expected_url
    # assert driver.current_url != old_expected_url
    print(f"Проверяем что фактический URL:\n{driver.current_url}\nсовпадает с ожидаемым:\n{expected_url}")


def test_always_fails(driver):
    driver.get("https://ru.wikipedia.org/wiki/%D0%A6%D0%B8%D1%86%D0%B5%D1%80%D0%BE%D0%BD")
    assert driver.title == "ASDJHALSKJDHIUHkJSHDJNSDKJHKSHDKSHD"  # Тест гарантировано упадет

def test_long_loading(driver):
    slow_url = "https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0"
    driver.get(slow_url)
    print(f"Открываем страницу {slow_url}")

    #time.sleep(15) - ОЧЕНЬ плохая реализация явного ожидания. Будет ждать независимо от того,
    # прогрузился элемент или нет

    # Хорошее явное ожидание:
    page_title = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "mw-page-title-main")))
    print(f"Используем явное ожидание для поиска элемента на странице: {page_title}")
    assert page_title.text == "Москва", f"Ожидали 'Москва', получили {page_title.text}"
    print(f"Проверка того, что ожидаемое название статьи: Москва\nсовпадает с фактическим: {page_title.text}")
