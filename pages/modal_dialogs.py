from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/modal-dialogs"
        super().__init__(driver, self.base_url)
        self.btns_modal_dialogs = WebElement(driver, " div:nth-child(3) > div > ul > li")
        self.icon = WebElement(driver, "#app > header > a")
        self.smal_modal = WebElement(driver, "#showSmallModal")
        self.large_modal = WebElement(driver, "#showLargeModal")
        self.close_smal_modal = WebElement(driver, "#closeSmallModal")
        self.close_large_modal = WebElement(driver, "#closeLargeModal")
        self.dialog_modal = WebElement(driver, "body > div.fade.modal.show > div")



