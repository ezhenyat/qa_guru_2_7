from selene.support.shared import browser
from selene import have


def select(item):
    browser.all('.custom-control-label').by(have.exact_text(item)).first.click()