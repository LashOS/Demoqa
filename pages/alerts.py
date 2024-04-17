from pages.base_page import BasePage
from components.components import WebElement


class Aletrs(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/alerts"
        super().__init__(driver, self.base_url)
        self.alet_btn = WebElement(driver, "#alertButton")
        self.confirm_btn = WebElement(driver, "#confirmButton")
        self.confirm_result = WebElement(driver, "#confirmResult")
        self.promtButton = WebElement(driver, "#promtButton")
        self.promptResult = WebElement(driver, "#promptResult")
        self.timerAlertButton = WebElement(driver, "#timerAlertButton")