import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_long_loading(driver):
    slow_url = "https://demoqa.com/checkbox"
    driver.get(slow_url)
    print(f"Открываем страницу {slow_url}")

    #time.sleep(15) - ОЧЕНЬ плохая реализация явного ожидания. Будет ждать независимо от того,
    # прогрузился элемент или нет
    # дописать
    # Хорошее явное ожидание:
    title_locator = (By.XPATH, "//h1[@class='text-center']")
    page_title = driver.find_element(*title_locator)   # Так будет падать из-за недостатка времени на поиск элемента
    # page_title = WebDriverWait(driver, 15).until(EC.presence_of_element_located(title_locator))
    print(f"Используем явное ожидание для поиска элемента на странице: {page_title}")
    assert page_title.text == "Check Box", f"Ожидали 'Check Box', получили {page_title.text}"
    print(f"Проверка того, что ожидаемое название статьи: Check Box\nсовпадает с фактическим: {page_title.text}")

# Взаимодействие с веб-элементами на странице: чек-боксы, раскрытие/скрытие дерева и т.п.
def test_web_elements(driver, web_page, base_page):
    demo_url = "https://demoqa.com/checkbox"
    driver.get(demo_url)
    print(f"Открываем страницу {demo_url}")

    driver.find_element(*web_page.plus_button).click()
    print(f"Клик на раскрытие дерева {driver.find_element(*web_page.plus_button)}")

    # 2 локатора для одного и того же элемента
    desktop_node_index = driver.find_element(By.XPATH, "(//span[@class='rct-checkbox'])[2]")
    desktop_node_label = driver.find_element(By.XPATH, "//label[@for='tree-node-desktop']")

    print(f"1: Desktop выбран: {desktop_node_index.is_selected()}")

    # if desktop_node_index.is_selected:
    #     desktop_node_index.click()
    #     print(f"2: Desktop выбран: {desktop_node_index.is_selected()}")

    desktop_node_index.click()
    print(f"Клик на первый локатор: {desktop_node_index}")

    # Локатор ИПУТА (самого чек-бокса и его значения: выбран или не выбран)
    desktop_node_input = driver.find_element(By.XPATH, "//input[@id='tree-node-desktop']")

    assert desktop_node_input.is_selected() == True, "Desktop: чек-бокс не выбран!"
    print(f"Проверка что чек-бокс Desktop выбран: {desktop_node_input.is_selected()}")

    desktop_node_label.click()
    print(f"Клик на второй локатор: {desktop_node_label}")

    assert desktop_node_label.is_selected() == False
    print("Проверка что чек-бокс Desktop деактивирован")

def test_double_click(driver, base_page, web_page):
    driver.get(web_page.web_el_url)
    print(f"Открываем страницу: {web_page.web_el_url}")

    expected_message = "You have done a double click"
    base_page.double_click(driver.find_element(*web_page.double_click_button))

    actual_message = driver.find_element(*web_page.double_click_message).text

    assert actual_message == expected_message
    print(f"Ожидали: {expected_message}\nПолучили: {actual_message}")

def test_right_click(driver, base_page, web_page):
    driver.get(web_page.web_el_url)
    print(f"Открываем страницу: {web_page.web_el_url}")

    expected_message = "You have done a right click"
    base_page.right_click(driver.find_element(*web_page.right_click_button))

    actual_message = driver.find_element(*web_page.right_click_message).text

    assert actual_message == expected_message
    print(f"Ожидали: {expected_message}\nПолучили: {actual_message}")

def test_calendar(driver, base_page, web_page):
    driver.get(web_page.calendar_url)
    print(f"Открываем страницу с календарем: {web_page.calendar_url}")

    test_date = (12, 21, 2024)
    web_page.set_calendar_date(*test_date)
    # web_page.set_calendar_date(2000, 3, 15)

    assert web_page.calendar_selector.text() in test_date
    print(f"Ожидаемая дата: {test_date}\nФактическая дата в календаре: {web_page.calendar_selector.text()}")




