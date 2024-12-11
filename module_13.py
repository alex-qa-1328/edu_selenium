from tests.login_tests.test_login import *
from tests.conftest import driver

# TODO: Основы Selenium Часть 2

'''
1. Негативное тестирование
    1.1 Проверяем текстовое содержимое элемента (ошибка, алерт, тост)
    1.2 Проверяем фактический URL-адрес
2. Обновление страницы
3. Имитация нажатия клавиш на клавиатуре
4. Создание скриншотов страницы
    4.1 Генерируем скриншоты с уникальным именем, отражающим текущую (на момент теста) дату и время
'''

# 1.1  1.2
test_invalid_login()

# 2
test_login_input_validation()

# 3
test_key_enter(driver)

# 4.1
test_always_fails(driver(request="1"))

