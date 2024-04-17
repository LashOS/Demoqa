import time
from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa


def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()
    assert modal_dialogs.btns_modal_dialogs.check_count_elements(5)


def test_navigation_modal(browser):
    navigation = ModalDialogs(browser)
    main_page = DemoQa(browser)

    navigation.visit()
    navigation.refresh()
    navigation.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    browser.refresh()
    time.sleep(2)
    assert main_page.equal_url()
    time.sleep(2)
    assert browser.title == "DEMOQA"
    browser.set_window_size(1000, 1000)
