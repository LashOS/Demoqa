import time

from pages.form_page import FormPage


def test_login_form_validate(browser):
    placeholder = FormPage(browser)
    placeholder.visit()

    placeholder.first_name.send_keys("Gosha")
    placeholder.last_name.send_keys("Tolmats")
    placeholder.user_name.send_keys("gosha@tolmats.com")
    placeholder.first_name.clear()
    placeholder.last_name.clear()
    placeholder.user_name.clear()
    time.sleep(3)
    assert placeholder.first_name.get_text() == ""
    assert placeholder.last_name.get_text() == ""
    assert placeholder.user_name.get_text() == ""
    assert placeholder.user_name.get_dom_attribute("pattern")
    placeholder.btn_submit.click_force()
    time.sleep(3)
    assert placeholder.user_form.get_dom_attribute("class") == "was-validated"
