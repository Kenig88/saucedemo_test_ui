import pytest
import allure

from data.links import Links


@allure.feature("Checkout Overview Page")
@pytest.mark.regression
class TestCheckoutOverviewPage:

    @allure.story("Отображение данных заказа")
    @allure.title("Пользователь видит добавленный товар на overview странице")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_sees_added_product_on_checkout_overview(self, opened_checkout_overview_page):
        opened_checkout_overview_page.is_opened()
        assert opened_checkout_overview_page.is_product_present("Sauce Labs Backpack")
        assert opened_checkout_overview_page.get_products_count() == 1

    @allure.story("Успешное завершение заказа")
    @allure.title("Пользователь может завершить checkout с overview страницы")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_finish_checkout(self, opened_checkout_overview_page):
        opened_checkout_overview_page.is_opened()
        opened_checkout_overview_page.click_finish()
        assert opened_checkout_overview_page.driver.current_url == Links.CHECKOUT_COMPLETE_PAGE

    @allure.story("Отмена checkout")
    @allure.title("Пользователь может отменить checkout и вернуться к products")
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_can_cancel_checkout_overview(self, opened_checkout_overview_page):
        opened_checkout_overview_page.is_opened()
        opened_checkout_overview_page.click_cancel()
        assert opened_checkout_overview_page.driver.current_url == Links.PRODUCTS_PAGE