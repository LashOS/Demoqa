import time

from pages.tables import Tables


def test_webtables(browser):
    web_tables = Tables(browser)

    web_tables.visit()
    web_tables.add.click()
    time.sleep(2)

    assert not web_tables.submit.click_force()
    time.sleep(2)
    web_tables.first_name.send_keys("Gosha")
    web_tables.last_name.send_keys("Tolmats")
    web_tables.email.send_keys("gosha@tolmats.com")
    web_tables.age.send_keys("30")
    web_tables.salary.send_keys("1000")
    web_tables.departament.send_keys("SPB")
    web_tables.submit.click()
    time.sleep(2)
    assert not web_tables.dialog_window.exist()
    time.sleep(2)
    assert web_tables.new_str.get_text() == "Gosha\nTolmats\n30\ngosha@tolmats.com\n1000\nSPB"
    web_tables.edit_new_str.click()
    assert web_tables.dialog_window.exist()
    web_tables.first_name.clear()
    web_tables.first_name.send_keys("Lesha")
    web_tables.submit.click()
    assert web_tables.new_str.get_text() == "Lesha\nTolmats\n30\ngosha@tolmats.com\n1000\nSPB"
    web_tables.btn_delete_gosha.click()
    assert web_tables.new_str.get_text() == "       "











