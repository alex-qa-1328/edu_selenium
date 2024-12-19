import datetime
from src.utils import calendar_util

from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage


class Web_Elements(BasePage):

    web_el_url = "https://demoqa.com/buttons"
    calendar_url = "https://demoqa.com/date-picker"

    # Локаторы:
    double_click_button = By.ID, "doubleClickBtn"
    right_click_button = (By.ID, "rightClickBtn")
    double_click_message = (By.ID, "doubleClickMessage")
    right_click_message = (By.ID, "rightClickMessage")

    plus_button = (By.XPATH, "//button[@title='Expand all']")
    minus_button = (By.XPATH, "//button[@title='Collapse all']")

    day = None
    # fixed_day = None
    calendar_selector = (By.ID, "datePickerMonthYearInput")
    calendar_month_picker = (By.CLASS_NAME, "react-datepicker__month-select")
    calendar_year_picker = (By.CLASS_NAME, "react-datepicker__year-select")

    def set_calendar_date(self, year, month, day):
        # Инд мес  0         1         2       3        4        5      6       7
        m = ["January", "February", "March", "April", "May", "June", "July", "August",
             #      8         9           10        11
             "September", "October", "November", "December"]

        self.driver.find_element(*self.calendar_selector).click()
        print("Открываем окно календаря")

        # self.driver.find_element(*self.calendar_year_picker).click()
        # print("Кликаем на выбор года")
        # self.driver.find_element(By.XPATH, f"//*/select/option[@value='{year}']").click()
        # print(f"Выбираем год: {year}")
        #
        # self.driver.find_element(*self.calendar_month_picker).click()
        # print("Кликаем на выбор месяца")
        # self.driver.find_element(By.XPATH, f"//select/option[@value='{month - 1}']").click()
        # print(f"Выбираем месяц: {m[month - 1]}")
                                                    # Choose Wednesday, December 4th, 2024

        day_of_week = calendar_util.day_of_week(year, month, day)
        print(f"Выбираем дату: {day_of_week}, {m[month - 1]} {day}, {year}]")
        # TODO: Дописать условие для weekends
        if day < 10:
            fixed_day = f"00{day}"
        else:
            fixed_day = f"0{day}"
        # self.driver.find_element(By.XPATH, f"//*[@aria-label=Choose {day_of_week}, {m[month - 1]} {day}th, {year}]").click()
        print(f"Локатор:\n//*[@class='react-datepicker__day react-datepicker__day--{fixed_day}']")
        self.driver.find_element(By.XPATH, f"//*[@class='react-datepicker__day react-datepicker__day--{fixed_day}']").click()
        # aria-label month day
        # print(f"Выбираем день: {day}")


