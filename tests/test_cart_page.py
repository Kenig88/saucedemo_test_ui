import pytest
import allure

from data.products_data import ProductNames


@allure.feature("Cart Page")
@pytest.mark.regression
class TestCartPage:

    @allure.story("Отображение товара в корзине")
    @allure.title("Пользователь видит добавленный товар в корзине")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "product_name",
        [
            ProductNames.BACKPACK,
            ProductNames.RED_TSHIRT,
        ],
        ids=[
            "popular-product",
            "edge-case-product-name",
        ]
    )
    def test_user_sees_added_product_in_cart(self, opened_cart_page_with_product, product_name, cart_page):
        cart_page = opened_cart_page_with_product(product_name)
        title = cart_page.is_opened()
        assert title == "Your Cart"
        assert cart_page.is_product_in_cart(product_name)

    @allure.story("Удаление товара")
    @allure.title("Пользователь может удалить товар из корзины")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "product_name",
        [
            ProductNames.BACKPACK,
            ProductNames.RED_TSHIRT,
        ],
        ids=[
            "popular-product",
            "edge-case-product-name",
        ]
    )
    def test_user_can_remove_product_from_cart(self, opened_cart_page_with_product, product_name, cart_page):
        cart_page = opened_cart_page_with_product(product_name)
        title = cart_page.is_opened()
        assert title == "Your Cart"
        assert cart_page.is_product_in_cart(product_name)
        cart_page.remove_from_cart(product_name)
        assert not cart_page.is_product_in_cart(product_name)
        assert cart_page.get_products_count() == 0

    @allure.story("Переход в checkout")
    @allure.title("Пользователь может перейти к оформлению заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_go_to_checkout_from_cart(
            self,
            opened_cart_page_with_product,
            checkout_info_page
            , cart_page):
        cart_page = opened_cart_page_with_product(ProductNames.BIKE_LIGHT)
        title = cart_page.is_opened()
        assert title == "Your Cart"
        cart_page.click_checkout()
        assert "checkout-step-one" in checkout_info_page.driver.current_url

    @allure.story("Возврат к товарам")
    @allure.title("Пользователь может вернуться к списку товаров")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_return_to_products_from_cart(self, opened_cart_page, products_page, cart_page):
        cart_page = opened_cart_page
        title = cart_page.is_opened()
        assert title == "Your Cart"
        cart_page.click_continue_shopping()
        assert "inventory" in products_page.driver.current_url

    @allure.story("Навигация")
    @allure.title("Пользователь может открыть подробности товара из корзины")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "product_name",
        [
            ProductNames.BACKPACK,
            ProductNames.RED_TSHIRT,
        ],
        ids=[
            "popular-product",
            "edge-case-product-name",
        ]
    )
    def test_user_can_open_product_details_from_cart(
            self,
            opened_cart_page_with_product,
            product_details_page,
            product_name
            , cart_page):
        cart_page = opened_cart_page_with_product(product_name)
        title = cart_page.is_opened()
        assert title == "Your Cart"
        assert cart_page.is_product_in_cart(product_name)
        cart_page.open_product_details(product_name)
        details_title = product_details_page.is_opened()
        assert details_title == product_name
