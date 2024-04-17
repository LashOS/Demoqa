from pages.demoqa import DemoQa
from pages.element import Element


def test_go_to_page_elements(browser):
    demo_qa_page = DemoQa(browser)
    el_page = Element(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.btn_click.click()
    assert el_page.equal_url()
