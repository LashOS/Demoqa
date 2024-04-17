from pages.element import Element


def test_find_elements(browser):
    el_page = Element(browser)
    el_page.visit()
    assert el_page.btns_first_menu.check_count_elements(9)
     