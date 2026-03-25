from selenium.webdriver.common.by import By
from data.links import Links
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    TITLE = (By.XPATH, "//span[text()='Checkout: Complete!']")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def __init__(self, driver):
        super().__init__(driver, url=Links.CHECKOUT_COMPLETE_PAGE)

    def is_opened(self) -> str:
        return self.assert_page_opened("checkout-complete", self.TITLE)

    def click_home_button(self) -> None:
        self.click(self.BACK_HOME_BUTTON)

    def get_complete_header_text(self) -> str:
        return self.get_text(self.COMPLETE_HEADER)

    def get_complete_text(self) -> str:
        return self.get_text(self.COMPLETE_TEXT)
