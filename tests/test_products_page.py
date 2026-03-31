import pytest
import allure

from config.products_data import ProductNames


@allure.feature("Products")
@pytest.mark.regression
class TestProductsPage:

    @allure.story("Добавление товара и навигация")
    @allure.title("Пользователь может добавить товар в корзину")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_add_product_to_cart(self, logged_in_products_page, cart_page):
        logged_in_products_page.add_to_cart(ProductNames.RED_TSHIRT)
        assert logged_in_products_page.get_cart_count() == 1
        logged_in_products_page.click_open_cart()
        assert cart_page.is_opened() == "Your Cart", "Страница CartPage не открылась"

    @allure.story("Удаление товара")
    @allure.title("Пользователь может удалить товар из корзины со страницы товаров")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_remove_product_from_products_page(self, logged_in_products_page):
        logged_in_products_page.add_to_cart(ProductNames.BIKE_LIGHT)
        assert logged_in_products_page.get_cart_count() == 1
        logged_in_products_page.remove_from_cart(ProductNames.BIKE_LIGHT)
        assert logged_in_products_page.get_cart_count() == 0

    @allure.story("Сортировка")
    @allure.title("Пользователь может отсортировать товары по цене")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "sort_value, reverse",
        [
            ("lohi", False),
            ("hilo", True),
        ],
        ids=[
            "price-low-to-high",
            "price-high-to-low",
        ]
    )
    def test_user_can_sort_products_by_price(self, logged_in_products_page, sort_value, reverse):
        logged_in_products_page.sort_by(sort_value)
        prices = logged_in_products_page.get_prices()
        assert prices == sorted(prices, reverse=reverse)

    @allure.story("Навигация")
    @allure.title("Пользователь может открыть карточку товара")
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_can_open_product_details(self, logged_in_products_page, product_details_page):
        logged_in_products_page.open_product_details(ProductNames.BACKPACK)
        assert product_details_page.is_opened(), "Страница ProductDetailsPage не открылась"
        assert product_details_page.get_product_name() == ProductNames.BACKPACK
