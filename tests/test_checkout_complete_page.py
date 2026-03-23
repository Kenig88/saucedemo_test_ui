import pytest
import allure

from data.links import Links
from data.checkout_data import CheckoutCompleteMessages


@allure.feature("Checkout Complete Page")
@pytest.mark.regression
class TestCheckoutCompletePage:

    @allure.story("Успешное завершение заказа")
    @allure.title("Пользователь видит подтверждение заказа и может вернуться к товарам")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_see_checkout_complete_page_and_return_to_products(self, opened_checkout_complete_page):
        title = opened_checkout_complete_page.is_opened()
        assert title == "Checkout: Complete!"
        assert opened_checkout_complete_page.driver.current_url == Links.CHECKOUT_COMPLETE_PAGE
        assert opened_checkout_complete_page.get_complete_header_text() == CheckoutCompleteMessages.HEADER
        assert opened_checkout_complete_page.get_complete_text() == CheckoutCompleteMessages.TEXT
        opened_checkout_complete_page.click_back_home()
        assert opened_checkout_complete_page.driver.current_url == Links.PRODUCTS_PAGE