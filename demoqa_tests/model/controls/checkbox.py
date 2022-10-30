from selene.support.shared import browser
from selene import have


def tick(*args):
    for arg in args:
        browser.all('.custom-checkbox').by(have.exact_text(arg)).first.click()