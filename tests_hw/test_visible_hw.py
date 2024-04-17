import time
from pages.accordion import Accordion


def test_visible_accordion(browser):
    elements = Accordion(browser)
    elements.visit()
    assert elements.el_1.visible()
    elements.el_2.click()
    time.sleep(2)
    assert not elements.el_1.visible()


def test_visible_accordion_default(browser):
    elements = Accordion(browser)
    elements.visit()
    assert not elements.el_3.visible()
    assert not elements.el_4.visible()
    assert not elements.el_5.visible()