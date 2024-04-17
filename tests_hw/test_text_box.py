import time

from pages.text_box import TextBox


def test_text_box(browser, text_name: str = "Gosha", text_current_address: str = "SPB"):
    test_text = TextBox(browser)
    test_text.visit()
    test_text.user_name.send_keys(text_name)
    test_text.current_address.send_keys(text_current_address)
    test_text.submit.click_force()
    time.sleep(2)

    assert test_text.output.get_text() == "Name:" + text_name + "\nCurrent Address :" + text_current_address




