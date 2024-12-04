import pytest
from pages.login_page import LoginPage


@pytest.mark.login
def test_valid_login(driver):
    driver.get("https://example.com/login")
    login_page = LoginPage(driver)

    # Perform login
    login_page.enter_username("test_user")
    login_page.enter_password("secure_password")
    login_page.click_login()

    # Verify successful login (add locator for post-login validation)
    assert "Welcome" in driver.title


@pytest.mark.login
def test_invalid_login(driver):
    driver.get("https://example.com/login")
    login_page = LoginPage(driver)

    # Attempt login with invalid credentials
    login_page.enter_username("wrong_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()

    # Verify error message
    assert login_page.get_error_message() == "Invalid credentials"
