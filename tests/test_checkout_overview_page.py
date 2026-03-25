import pytest
import allure


@allure.feature("Checkout Overview Page")
@pytest.mark.regression
class TestCheckoutOverviewPage:

    @allure.story("Отображение данных заказа")
    @allure.title("Пользователь видит добавленный товар на overview странице")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_sees_added_product_on_checkout_overview(self, opened_checkout_overview_page):
        assert opened_checkout_overview_page.has_any_product()
        assert opened_checkout_overview_page.get_products_count() >= 1

    @allure.story("Успешное завершение заказа")
    @allure.title("Пользователь может завершить checkout с overview страницы")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_finish_checkout(self, opened_checkout_overview_page, checkout_complete_page):
        opened_checkout_overview_page.click_finish()
        assert checkout_complete_page.is_opened()

    @allure.story("Отмена checkout")
    @allure.title("Пользователь может отменить checkout и вернуться к products")
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_can_cancel_checkout_overview(self, opened_checkout_overview_page, products_page):
        opened_checkout_overview_page.click_cancel()
        assert products_page.is_opened()
