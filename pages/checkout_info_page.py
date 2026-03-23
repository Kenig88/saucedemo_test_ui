from selenium.webdriver.common.by import By
from data.links import Links
from pages.base_page import BasePage


class CheckoutInfoPage(BasePage):
    TITLE = (By.XPATH, "//span[text()='Checkout: Your Information']")

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver, url=Links.CHECKOUT_INFO_PAGE)

    def is_opened(self) -> str:
        return self.assert_page_opened("checkout-step-one", self.TITLE)

    def enter_first_name(self, first_name: str) -> None:
        self.enter_text(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name: str) -> None:
        self.enter_text(self.LAST_NAME_INPUT, last_name)

    def enter_postal_code(self, postal_code: str) -> None:
        self.enter_text(self.POSTAL_CODE_INPUT, postal_code)

    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_continue_button(self) -> None:
        self.click(self.CONTINUE_BUTTON)

    def click_cancel_button(self) -> None:
        self.click(self.CANCEL_BUTTON)

    def error_message_text(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)