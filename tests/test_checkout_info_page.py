import pytest
import allure

from data.checkout_data import CheckoutInfoData, ErrorMessagesCheckoutInfo
from data.links import Links


@allure.feature("Checkout Step One Page")
@pytest.mark.regression
class TestCheckoutInfoPage:

    @allure.story("Успешное заполнение checkout формы")
    @allure.title("Пользователь может перейти к overview с валидными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_continue_checkout_with_valid_data(self, opened_checkout_info_page):
        opened_checkout_info_page.is_opened()
        opened_checkout_info_page.fill_checkout_form(
            CheckoutInfoData.FIRST_NAME,
            CheckoutInfoData.LAST_NAME,
            CheckoutInfoData.POSTAL_CODE,
        )
        opened_checkout_info_page.click_continue_button()
        assert opened_checkout_info_page.driver.current_url == Links.CHECKOUT_OVERVIEW_PAGE

    @allure.story("Валидация обязательных полей")
    @allure.title("Пользователь видит ошибки при пустых обязательных полях")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "first_name, last_name, postal_code, expected_error",
        [
            (
                    None,
                    CheckoutInfoData.LAST_NAME,
                    CheckoutInfoData.POSTAL_CODE,
                    ErrorMessagesCheckoutInfo.EMPTY_FIRST_NAME,
            ),
            (
                    CheckoutInfoData.FIRST_NAME,
                    None,
                    CheckoutInfoData.POSTAL_CODE,
                    ErrorMessagesCheckoutInfo.EMPTY_LAST_NAME,
            ),
            (
                    CheckoutInfoData.FIRST_NAME,
                    CheckoutInfoData.LAST_NAME,
                    None,
                    ErrorMessagesCheckoutInfo.EMPTY_POSTAL_CODE,
            ),
        ],
        ids=[
            "empty-first-name",
            "empty-last-name",
            "empty-postal-code",
        ]
    )
    def test_user_sees_error_with_empty_required_fields(
        self,
        opened_checkout_info_page,
        first_name,
        last_name,
        postal_code,
        expected_error,
    ):
        opened_checkout_info_page.is_opened()
        if first_name:
            opened_checkout_info_page.enter_first_name(first_name)
        if last_name:
            opened_checkout_info_page.enter_last_name(last_name)
        if postal_code:
            opened_checkout_info_page.enter_postal_code(postal_code)
        opened_checkout_info_page.click_continue_button()
        assert opened_checkout_info_page.driver.current_url == Links.CHECKOUT_INFO_PAGE
        assert opened_checkout_info_page.error_message_text() == expected_error

    @allure.story("Отмена checkout")
    @allure.title("Пользователь может отменить заполнение формы и вернуться в cart")
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_can_cancel_checkout(self, opened_checkout_info_page):
        opened_checkout_info_page.is_opened()
        opened_checkout_info_page.click_cancel_button()
        assert opened_checkout_info_page.driver.current_url == Links.CART_PAGE