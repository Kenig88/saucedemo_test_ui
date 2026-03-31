import pytest
import allure

from config.products_data import ProductNames


@allure.feature("Cart")
@pytest.mark.regression
class TestCartPage:

    @allure.story("Отображение товара в корзине")
    @allure.title("Пользователь видит добавленный товар в корзине")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_sees_added_product_in_cart(self, cart_page_with_product):
        page = cart_page_with_product(ProductNames.RED_TSHIRT)
        assert page.is_product_in_cart(ProductNames.RED_TSHIRT)

    @allure.story("Удаление товара")
    @allure.title("Пользователь может удалить товар из корзины")
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_can_remove_product_from_cart(self, cart_page_with_product):
        page = cart_page_with_product(ProductNames.BIKE_LIGHT)
        assert page.is_product_in_cart(ProductNames.BIKE_LIGHT)
        page.remove_from_cart(ProductNames.BIKE_LIGHT)
        assert not page.is_product_in_cart(ProductNames.BIKE_LIGHT)

    @allure.story("Переход в checkout")
    @allure.title("Пользователь может перейти к оформлению заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_go_to_checkout_from_cart(self, cart_page_with_product, checkout_info_page):
        page = cart_page_with_product(ProductNames.BACKPACK)
        page.click_checkout()
        assert checkout_info_page.is_opened() == "Checkout: Your Information", "Страница CheckoutInfoPage не открылась"

    @allure.story("Возврат к товарам")
    @allure.title("Пользователь может вернуться к списку товаров")
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_can_return_to_products_from_cart(self, cart_page_with_product, products_page):
        page = cart_page_with_product(ProductNames.RED_TSHIRT)
        page.click_continue_shopping()
        assert products_page.is_opened() == "Products", "Страница ProductsPage не открылась"
