from tests.conftest import driver
from tests.login_tests.test_login import test_long_loading
from tests.web_elements_tests.test_web_elements import *

# TODO: Модуль 14. Детали Selenium и Практика


# 1.1 Неявное - имплицитное ожидание.
driver()

# 1.2 Явное ожидание (конкретного условия или элемента)
test_long_loading()

# 1.3 Взаимодействие с чекбоксами
test_web_elements()


# 2. ActionChains
# 2.1 Двойной клик (левой кнопкой мыши)

# 2.2 Клик правой кнопкой мыши
test_double_click()


# 3.
# 4.


