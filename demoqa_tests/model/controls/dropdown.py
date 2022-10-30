from selene.support.shared import browser
from selene import have, command


def select(element, option):
    browser.element(element).click()
    browser.all('[id^=react-select][id*=-option-]').by(
        have.exact_text(option)
    ).first.click()