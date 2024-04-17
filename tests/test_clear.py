import time
from pages.text_box import TextBox


def test_clear(browser):
    clear_box = TextBox(browser)
    clear_box.visit()
    clear_box.user_name.send_keys("Gosha")
    time.sleep(2)
    clear_box.user_name.clear()
    time.sleep(2)
    assert clear_box.user_name.get_text() == ""
