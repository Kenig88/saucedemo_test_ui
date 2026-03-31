from selenium.webdriver.common.by import By
from config.links import Links
from pages.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.XPATH, "//span[text()='Your Cart']")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        super().__init__(driver, url=Links.CART_PAGE)

    def is_opened(self) -> str:
        return self.assert_page_opened("cart", self.TITLE)

    def remove_from_cart(self, product_name: str) -> None:
        remove_button = (
            By.XPATH,
            f"//div[contains(@class, 'cart_item')]"
            f"[.//*[contains(@class, 'inventory_item_name') and normalize-space()='{product_name}']]"
            f"//button"
        )
        self.click(remove_button)

    def click_continue_shopping(self) -> None:
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def click_checkout(self) -> None:
        self.click(self.CHECKOUT_BUTTON)

    def get_products_count(self) -> int:
        return self.get_elements_count(self.CART_ITEM)

    def get_product_names(self) -> list[str]:
        return [element.text for element in self.find_all(self.PRODUCT_NAME)]

    def is_product_in_cart(self, product_name: str) -> bool:
        return product_name in self.get_product_names()
