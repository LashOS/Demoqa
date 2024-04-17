from pages.text_box import TextBox


def test_css(browser):
    css_check = TextBox(browser)
    css_check.visit()
    assert css_check.submit.check_css("color", "rgba(255, 255, 255, 1)")
    assert css_check.submit.check_css("backgroundColor", "rgba(0, 123, 255, 1)")
    assert css_check.submit.check_css("borderColor", "rgb(0, 123, 255)")
