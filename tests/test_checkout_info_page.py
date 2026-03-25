import pytest
import allure

from data.checkout_data import CheckoutInfoData, ErrorMessagesCheckoutInfo


@allure.feature("Checkout Step One")
@pytest.mark.regression
class TestCheckoutInfoPage:

    @allure.story("Успешное заполнение checkout формы")
    @allure.title("Пользователь может перейти к overview с валидными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_continue_checkout_with_valid_data(self, opened_checkout_info_page, checkout_overview_page):
        opened_checkout_info_page.enter_checkout_form(
            first_name=CheckoutInfoData.FIRST_NAME,
            last_name=CheckoutInfoData.LAST_NAME,
            postal_code=CheckoutInfoData.POSTAL_CODE
        )
        opened_checkout_info_page.click_continue_button()
        assert checkout_overview_page.is_opened()

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
                    ErrorMessagesCheckoutInfo.EMPTY_FIRST_NAME
            ),
            (
                    CheckoutInfoData.FIRST_NAME,
                    None,
                    CheckoutInfoData.POSTAL_CODE,
                    ErrorMessagesCheckoutInfo.EMPTY_LAST_NAME
            ),
            (
                    CheckoutInfoData.FIRST_NAME,
                    CheckoutInfoData.LAST_NAME,
                    None,
                    ErrorMessagesCheckoutInfo.EMPTY_POSTAL_CODE
            )
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
            expected_error
    ):
        if first_name:
            opened_checkout_info_page.enter_first_name(first_name)
        if last_name:
            opened_checkout_info_page.enter_last_name(last_name)
        if postal_code:
            opened_checkout_info_page.enter_postal_code(postal_code)
        opened_checkout_info_page.click_continue_button()
        assert opened_checkout_info_page.error_message_text() == expected_error

    @allure.story("Отмена checkout")
    @allure.title("Пользователь может отменить заполнение формы и вернуться в cart")
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_can_cancel_checkout(self, opened_checkout_info_page, cart_page):
        opened_checkout_info_page.click_cancel_button()
        assert cart_page.is_opened()
