import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver(request):
    # Initialize Chrome WebDriver with options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    driver.implicitly_wait(10)  # имплицитное (неявное) ожидание заставляет WebDriver
    # опрашивать DOM определенное количество времени, когда пытается найти элемент.
    # по сути ожидание любого элемента ДО 10 секунд (если элемент найден, продолжает выполнять работу дальше)
    request.node._driver = driver
    yield driver
    driver.quit()


def pytest_exception_interact(node, call, report):
    if report.failed:
        driver = getattr(node, "_driver", None)
        if driver:
            # Сохраняем скриншот
            screenshot_path = os.path.join(f"C:/Users/Alexandr/PycharmProjects/edu_selenium"
                                           f"/src/screenshots/{datetime.now().strftime("%H-%M-%S-%d-%m-%Y")}_{node.name}.png")
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
