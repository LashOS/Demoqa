import time

from pages.demoqa import DemoQa
from pages.accordion import Accordion
from pages.alerts import Aletrs
from pages.browser_tab import BrowserTab
import pytest


def test_seo(browser):
    demo = DemoQa(browser)

    demo.visit()
    assert browser.title() == "DEMOQA"


@pytest.mark.parametrize("pages", [Accordion, Aletrs, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == "DEMOQA"


