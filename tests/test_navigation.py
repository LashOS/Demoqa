import time
from pages.demoqa import DemoQa
from pages.element import Element
def test_navigation(browser):
    demo = DemoQa(browser)
    elements = Element(browser)

    demo.visit()
    demo.button_elements.click()

    elements.refresh()
    browser.refresh()

    browser.back()
    browser.forward()
    assert elements.equal_url()





