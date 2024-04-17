from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/webtables"
        super().__init__(driver, self.base_url)
        self.no_data = WebElement(driver, "div.rt-noData")
        self.btn_delete_row = WebElement(driver, "[data-toggle='tooltip'][title='Delete']")
        self.add = WebElement(driver, "#addNewRecordButton")
        self.submit = WebElement(driver, "#submit")
        self.first_name = WebElement(driver, "#firstName")
        self.last_name = WebElement(driver, "#lastName")
        self.email = WebElement(driver, "#userEmail")
        self.age = WebElement(driver, "#age")
        self.salary = WebElement(driver, "#salary")
        self.departament = WebElement(driver, "#department")
        self.dialog_window = WebElement(driver, "body > div.fade.modal.show > div > div")
        self.new_str = WebElement(driver, "div.rt-tbody > div:nth-child(4) > div")
        self.edit_new_str = WebElement(driver, "#edit-record-4")
        self.btn_delete_gosha = WebElement(driver, "#delete-record-4")
        # self.sort_first_name = WebElement(driver, "div.rt-thead.-header > div:first-child")
        # self.sort_last_name = WebElement(driver, "div.rt-thead.-header > div:second-child")
        # self.sort_email = WebElement(driver, "div.rt-thead.-header > div:third-child")
        # self.sort_age = WebElement(driver, "div.rt-thead.-header > div:fourth-child")
        # self.sort_salary = WebElement(driver, "div.rt-thead.-header > div:fifth-child")
        # self.sort_departament = WebElement(driver, "div.rt-thead.-header > div:sixth-child")
        self.sort_first_name = WebElement(driver, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(1)")
        self.sort_last_name = WebElement(driver, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(2)")
        self.sort_email = WebElement(driver, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(4)")
        self.sort_age = WebElement(driver, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(3)")
        self.sort_salary = WebElement(driver, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(5)")
        self.sort_departament = WebElement(driver, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(6)")

