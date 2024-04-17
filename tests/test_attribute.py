from pages.text_box import TextBox


def test_placeholder(browser):
    test_box = TextBox(browser)

    test_box.visit()
    assert test_box.user_name.get_dom_attribute("placeholder") == "Full Name"

