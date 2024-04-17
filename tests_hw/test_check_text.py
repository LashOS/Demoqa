from pages.demoqa import DemoQa
from pages.element import Element


def test_check_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.footer_text.get_text() == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."


def test_check_text_please(browser):
    demo_qa_page = DemoQa(browser)
    el_page = Element(browser)
    demo_qa_page.visit()
    demo_qa_page.button_elements.click()
    assert el_page.please_text.get_text() == "Please select an item from left to start practice."


def test_page_elements(browser):
    el_page = Element(browser)
    el_page.visit()

    assert el_page.text_elements.get_text() == "Elements"
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()


