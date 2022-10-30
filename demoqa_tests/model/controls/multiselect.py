from selene.support.shared import browser
from selene import have


def choose(element, *args):
    for arg in args:
        browser.element(element).type(arg).press_enter()