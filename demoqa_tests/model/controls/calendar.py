from selene.support.shared import browser
from selene import have, command


def fill_by_input(element, value):
    browser.element(element).perform(command.js.set_value(value))


def fill_by_datepicker(element, day, month, year):
    browser.element(element).click()
    browser.element('.react-datepicker__year-select').send_keys(year)
    browser.element('.react-datepicker__month-select').send_keys(month)
    browser.element(f'.react-datepicker__day--0{day}'f':not(.react-datepicker__day--outside-month)').click()

