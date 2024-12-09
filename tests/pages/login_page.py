from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage


class LoginPage(BasePage):

    # Локаторы
    username_input = (By.XPATH, "//input[@id='wpName1']")
    password_input = (By.ID, "wpPassword1")
    login_button = (By.ID, "pt-login")
    error_message = (By.XPATH, "//*[@class='cdx-message__content']")
    submit_button = (By.ID, 'wpLoginAttempt')
    # submit_button = (By.XPATH, "//*[@id='wpLoginAttempt']")
    username_element = (By.ID, "pt-userpage")

    with open(r'C:\Users\Alexandr\PycharmProjects\edu_selenium\src\users.txt', "r") as file:
        line = file.readline().strip()
        valid_username, valid_password = line.split(",")    # ctrl + D дублирует строку или выделенную область; ctrl + / комментирует строку

    with open(r'C:\Users\Alexandr\PycharmProjects\edu_selenium\src\negative_users.txt', 'r') as neg_file:
        n_line = neg_file.readline().strip()
        invalid_username, invalid_password = n_line.split(",")

    @staticmethod
    def login_data():
        with open(r"C:\Users\Alexandr\PycharmProjects\edu_selenium\src\logins.txt", "r") as logins_file:
            # Read logins, stripping whitespace or newline characters
            return [login.strip() for login in logins_file.readlines()]


    main_page_url = "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
    negative_url = "https://ru.wiipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"

    def open_url(self):
        self.driver.get(self.main_page_url)

    def login(self, login, password):
        self.open_url()
        print(f"Открывается страница: {self.main_page_url}\n")

        self.driver.find_element(*self.login_button).click()
        print("Клик на кнопку войти")
        self.driver.find_element(*self.username_input).send_keys(login)
        self.driver.find_element(*self.password_input).send_keys(password)
        print(f"Ввод логина и пароля:\n{login}\n{password}")
        self.driver.find_element(*self.submit_button).click()
        print("Нажатие кнопки войти после ввода данных")


    def get_error_message(self):
        return self.get_element_text(self.error_message)
