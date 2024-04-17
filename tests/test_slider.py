from selenium.webdriver import Keys

from pages.slider import Slider

def test_slider(browser):
    page_slider = Slider(browser)

    page_slider.visit()
    assert page_slider.slider.exist()

    while not page_slider.inp.get_dom_attribute("value") == "50":
        page_slider.slider.send_keys(Keys.ARROW_RIGHT)

    assert page_slider.inp.get_dom_attribute("value") == "50"



