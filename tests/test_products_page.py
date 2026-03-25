import pytest
import allure

from data.products_data import ProductNames


@allure.feature("Products")
@pytest.mark.regression
class TestProductsPage:

    @allure.story("Добавление товара и навигация")
    @allure.title("Пользователь может добавить товар в корзину")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_add_product_to_cart(self, opened_products_page_after_login, cart_page):
        opened_products_page_after_login.add_to_cart(ProductNames.RED_TSHIRT)
        assert opened_products_page_after_login.get_cart_count() == 1
        opened_products_page_after_login.click_open_cart()
        assert cart_page.is_opened()

    @allure.story("Удаление товара")
    @allure.title("Пользователь может удалить товар из корзины со страницы товаров")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_remove_product_from_products_page(self, opened_products_page_after_login):
        opened_products_page_after_login.add_to_cart(ProductNames.BIKE_LIGHT)
        assert opened_products_page_after_login.get_cart_count() == 1
        opened_products_page_after_login.remove_from_cart(ProductNames.BIKE_LIGHT)
        assert opened_products_page_after_login.get_cart_count() == 0

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
    def test_user_can_sort_products_by_price(self, opened_products_page_after_login, sort_value, reverse):
        opened_products_page_after_login.sort_by(sort_value)
        prices = opened_products_page_after_login.get_prices()
        assert prices == sorted(prices, reverse=reverse)


    # игнорируется, не доделан
    @pytest.mark.skipif
    @allure.story("Навигация")
    @allure.title("Пользователь может открыть карточку товара")
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_can_open_product_details(self, opened_products_page_after_login, product_details_page, product_name):
        opened_products_page_after_login.open_product_details(product_name)
        assert product_details_page.is_opened()