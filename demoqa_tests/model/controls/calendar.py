from sys import platform
from selene.support.shared import browser
from selenium.webdriver.common.keys import Keys
from selene import have, command


def fill_by_input(element, value):
    if platform == 'darwin':
        browser.element(element).click().send_keys(Keys.COMMAND + 'a').type(value).press_enter()
    else:
        browser.element(element).click().send_keys(Keys.CONTROL + 'a').type(value).press_enter()


def fill_by_datepicker(element, day, month, year):
    browser.element(element).click()
    browser.element('.react-datepicker__year-select').send_keys(year)
    browser.element('.react-datepicker__month-select').send_keys(month)
    browser.element(f'.react-datepicker__day--0{day}'f':not(.react-datepicker__day--outside-month)').click()
