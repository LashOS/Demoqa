from pages.base_page import BasePage
from components.components import WebElement


class DemoQa(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/"
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, "#app > header > a")
        self.btn_click = WebElement(driver, "#app > div > div > div.home-body > div > div:nth-child(1)")
        self.footer_text = WebElement(driver, "span")
        self.button_elements = WebElement(driver, "div:nth-child(1) > div > div.avatar.mx-auto.white > svg > path")
