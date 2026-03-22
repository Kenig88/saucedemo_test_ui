from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    TITLE = (By.CLASS_NAME, "inventory_details_name")

    def is_opened(self) -> str:
        return self.find(self.TITLE).text