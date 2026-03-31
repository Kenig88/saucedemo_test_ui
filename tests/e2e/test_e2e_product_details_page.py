import allure
import pytest

from config.products_data import ProductNames
from config.checkout_data import CheckoutInfoData, CheckoutCompleteMessages


@allure.feature("E2E")
@pytest.mark.e2e
@allure.title("Пользователь может пройти полный цикл checkout flow")
@allure.severity(allure.severity_level.BLOCKER)
def test_checkout_flow(
        logged_in_products_page,
        products_page,
        product_details_page,
        cart_page,
        checkout_info_page,
        checkout_overview_page,
        checkout_complete_page
):
    product_name = ProductNames.RED_TSHIRT

    with allure.step("Открыта Products page"):
        assert products_page.is_opened() == "Products", "Страница ProductsPage не открылась"

    with allure.step("Пользователь открывает страницу деталей товара"):
        products_page.open_product_details(product_name)
        assert product_details_page.is_opened(), "Страница ProductDetailsPage не открылась"
        assert product_details_page.get_product_name() == product_name

    with allure.step("Пользователь добавляет товар в корзину со страницы деталей"):
        product_details_page.add_to_cart()
        assert product_details_page.get_cart_count() == 1

    with allure.step("Пользователь переходит в корзину"):
        product_details_page.click_open_cart()
        assert cart_page.is_opened() == "Your Cart", "Страница CartPage не открылась"
        assert cart_page.get_products_count() == 1
        assert cart_page.is_product_in_cart(product_name)

    with allure.step("Пользователь переходит к checkout"):
        cart_page.click_checkout()
        assert checkout_info_page.is_opened() == "Checkout: Your Information", "Страница CheckoutInfoPage не открылась"

    with allure.step("Пользователь заполняет checkout форму"):
        checkout_info_page.enter_checkout_form(
            first_name=CheckoutInfoData.FIRST_NAME,
            last_name=CheckoutInfoData.LAST_NAME,
            postal_code=CheckoutInfoData.POSTAL_CODE
        )
        checkout_info_page.click_continue_button()

    with allure.step("Пользователь проверяет overview и завершает заказ"):
        assert checkout_overview_page.is_opened() == "Checkout: Overview", "Страница CheckoutOverviewPage не открылась"
        assert checkout_overview_page.get_products_count() == 1
        checkout_overview_page.click_finish()

    with allure.step("Пользователь видит успешное завершение заказа"):
        assert checkout_complete_page.is_opened() == "Checkout: Complete!", "Страница CheckoutCompletePage не открылась"
        assert checkout_complete_page.get_complete_header_text() == CheckoutCompleteMessages.HEADER
        assert checkout_complete_page.get_complete_text() == CheckoutCompleteMessages.TEXT

    with allure.step("Пользователь возвращается на страницу товаров"):
        checkout_complete_page.click_home_button()
        assert products_page.is_opened() == "Products", "Страница ProductsPage не открылась"
        assert products_page.get_cart_count() == 0
