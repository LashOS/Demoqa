import time
import requests
import pytest
from pages.modal_dialogs import ModalDialogs


def test_check_modal(browser):
    page_modal = ModalDialogs(browser)
    url = page_modal.base_url
    response = requests.get(url)
    if response.status_code == 200:
        assert True
    else:
        pytest.skip(f"Page {url} is not accessible")

    page_modal.visit()
    page_modal.smal_modal.click()
    time.sleep(2)
    assert page_modal.dialog_modal.exist()
    page_modal.close_smal_modal.click()
    time.sleep(2)
    assert not page_modal.dialog_modal.exist()
    time.sleep(2)
    page_modal.large_modal.click()
    time.sleep(2)
    assert page_modal.dialog_modal.exist()
    page_modal.close_large_modal.click()
    time.sleep(2)
    assert not page_modal.dialog_modal.exist()


