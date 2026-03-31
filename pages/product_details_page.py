from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.links import Links


class ProductDetailsPage(BasePage):
    PRODUCT_TITLE = (By.CLASS_NAME, "inventory_details_name")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart")
    CART = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        super().__init__(driver, url=Links.PRODUCTS_DETAILS_PAGE)

    def is_opened(self) -> str:
        return self.assert_page_opened("inventory-item.html", self.PRODUCT_TITLE)

    def get_product_name(self) -> str:
        return self.get_text(self.PRODUCT_TITLE)

    def add_to_cart(self) -> None:
        self.click(self.ADD_TO_CART_BUTTON)

    def get_cart_count(self) -> int:
        badges = self.find_all(self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def click_open_cart(self) -> None:
        self.click(self.CART)
