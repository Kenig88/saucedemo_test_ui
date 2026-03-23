from selenium.webdriver.common.by import By
from data.links import Links
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    TITLE = (By.XPATH, "//span[text()='Checkout: Overview']")
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    TOTAL_PRICE_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        super().__init__(driver, url=Links.CHECKOUT_OVERVIEW_PAGE)

    def is_opened(self) -> str:
        return self.assert_page_opened("checkout-step-two", self.TITLE)

    def click_finish(self) -> None:
        self.click(self.FINISH_BUTTON)

    def click_cancel(self) -> None:
        self.click(self.CANCEL_BUTTON)

    def get_products_count(self) -> int:
        return self.get_elements_count(self.CART_ITEM)

    def get_product_names(self) -> list[str]:
        return [
            element.text
            for element in self.find_all(self.PRODUCT_NAME)
        ]

    def is_product_present(self, product_name: str) -> bool:
        return product_name in self.get_product_names()

    def get_total_label_text(self) -> str:
        return self.get_text(self.TOTAL_PRICE_LABEL)