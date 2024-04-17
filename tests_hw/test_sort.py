import time

from pages.tables import Tables


def test_sort(browser):
    web_tables = Tables(browser)
    elements = [web_tables.sort_first_name, web_tables.sort_last_name, web_tables.sort_email, web_tables.sort_age, web_tables.sort_salary, web_tables.sort_departament]
    web_tables.visit()

    for element in elements:
        element.click()
        time.sleep(2)
        assert element.get_dom_attribute("class") == "rt-th rt-resizable-header -sort-asc -cursor-pointer"
        element.click()
        time.sleep(2)
        assert element.get_dom_attribute("class") == "rt-th rt-resizable-header -sort-desc -cursor-pointer"
