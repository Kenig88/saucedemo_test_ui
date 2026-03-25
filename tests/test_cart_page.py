import pytest
import allure

from data.products_data import ProductNames


@allure.feature("Cart")
@pytest.mark.regression
class TestCartPage:

    @allure.story("Отображение товара в корзине")
    @allure.title("Пользователь видит добавленный товар в корзине")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_sees_added_product_in_cart(self, product_in_cart_product_name):
        page = product_in_cart_product_name(ProductNames.RED_TSHIRT)
        assert page.is_product_in_cart(ProductNames.RED_TSHIRT)

    @allure.story("Удаление товара")
    @allure.title("Пользователь может удалить товар из корзины")
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_can_remove_product_from_cart(self, product_in_cart_product_name):
        page = product_in_cart_product_name(ProductNames.BIKE_LIGHT)
        assert page.is_product_in_cart(ProductNames.BIKE_LIGHT)
        page.remove_from_cart(ProductNames.BIKE_LIGHT)
        assert not page.is_product_in_cart(ProductNames.BIKE_LIGHT)

    @allure.story("Переход в checkout")
    @allure.title("Пользователь может перейти к оформлению заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_go_to_checkout_from_cart(self, product_in_cart_product_name, checkout_info_page):
        page = product_in_cart_product_name(ProductNames.BACKPACK)
        page.click_checkout()
        assert checkout_info_page.is_opened()

    @allure.story("Возврат к товарам")
    @allure.title("Пользователь может вернуться к списку товаров")
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_can_return_to_products_from_cart(self, product_in_cart_product_name, products_page):
        page = product_in_cart_product_name(ProductNames.RED_TSHIRT)
        page.click_continue_shopping()
        assert products_page.is_opened()
