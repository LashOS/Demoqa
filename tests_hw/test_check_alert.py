import time

from pages.alerts import Aletrs


def test_check_alert(browser):
    page_alert = Aletrs(browser)

    page_alert.visit()
    page_alert.timerAlertButton.click()
    time.sleep(7)
    assert page_alert.alert()