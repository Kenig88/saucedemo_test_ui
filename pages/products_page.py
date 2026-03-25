from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from data.links import Links
from pages.base_page import BasePage


class ProductsPage(BasePage):
    TITLE = (By.XPATH, "//span[text()='Products']")
    CART = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    PRODUCT = (By.CLASS_NAME, "inventory_item")
    PRICE = (By.CLASS_NAME, "inventory_item_price")
    SORT = (By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver):
        super().__init__(driver, url=Links.PRODUCTS_PAGE)

    def is_opened(self) -> str:
        return self.assert_page_opened("inventory", self.TITLE)

    def _get_product_card(self, product_name: str):
        locator = (
            By.XPATH,
            f"//div[contains(@class, 'inventory_item')]"
            f"[.//*[contains(@class, 'inventory_item_name') and normalize-space()='{product_name}']]"
        )
        return self.find(locator)

    def _click_product_button(self, product_name: str) -> None:
        product_card = self._get_product_card(product_name)
        button = product_card.find_element(By.TAG_NAME, "button")
        button.click()

    def add_to_cart(self, product_name: str) -> None:
        self._click_product_button(product_name)

    def remove_from_cart(self, product_name: str) -> None:
        self._click_product_button(product_name)

    def open_product_details(self, product_name: str) -> None:
        locator = (
            By.XPATH,
            f"//*[contains(@class, 'inventory_item_name') and normalize-space()='{product_name}']"
        )
        self.click(locator)

    def click_open_cart(self) -> None:
        self.click(self.CART)

    def sort_by(self, value: str) -> None:
        Select(self.find(self.SORT)).select_by_value(value)

    def get_products_count(self) -> int:
        return self.get_elements_count(self.PRODUCT)

    def get_cart_count(self) -> int:
        badges = self.find_all(self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def get_prices(self) -> list[float]:
        return [
            float(price.text.replace("$", ""))
            for price in self.find_all(self.PRICE)
        ]
