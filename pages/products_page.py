from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from data.links import Links
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, url=Links.PRODUCTS_PAGE)

    # локаторы:

    TITLE = (By.XPATH, "//span[text()='Products']")
    CART = (By.ID, "shopping_cart_container")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    PRODUCT = (By.CLASS_NAME, "inventory_item")
    PRICE = (By.CLASS_NAME, "inventory_item_price")
    SORT = (By.CLASS_NAME, "product_sort_container")

    # методы:

    # страница открыта
    def is_opened(self) -> str:
        return self.assert_page_opened("inventory", self.TITLE)

    # добавить в корзину
    def add_to_cart(self, name):
        """
        Нажать кнопку Add to cart для товара с названием `name`.
        Ищем кнопку внутри карточки товара по тексту.
        """
        # находим карточку товара по названию
        product_card = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH,
                 f"//div[@class='inventory_item']//div[text()='{name}']/ancestor::div[@class='inventory_item']"))
        )
        # ищем кнопку внутри карточки
        button = product_card.find_element(By.TAG_NAME, "button")
        button.click()

    # посмотреть детали продукта
    def click_open_product(self, product_name: str) -> None:
        locator = (By.XPATH, f"//div[text()='{product_name}']")
        self.click(locator)

    # перейти в корзину
    def click_open_cart(self) -> None:
        self.click(self.CART)

    # сортировка
    def sort_by(self, value: str) -> None:
        select = Select(self.find(self.SORT))
        select.select_by_value(value)

    # получить список товаров
    def get_products_count(self) -> int:
        return self.get_elements_count(self.PRODUCT)

    # счетчик корзины
    def get_cart_count(self) -> int:
        elements = self.find_all(self.CART_BADGE)
        return int(elements[0].text) if elements else 0

    # получить цены
    def get_prices(self) -> list[float]:
        elements = self.find_all(self.PRICE)
        prices = []
        for e in elements:
            prices.append(float(e.text.replace("$", "")))
        return prices
