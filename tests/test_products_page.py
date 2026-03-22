import pytest
import allure


@allure.feature("Products Page")
@pytest.mark.regression
class TestProductsPage:

    @allure.story("Открытие страницы")
    @allure.title("Страница товаров успешно открывается")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_products_page_opened(self, login, products_page):
        title = products_page.is_opened()
        assert title == "Products"

    @allure.story("Добавление товара")
    @allure.title("Пользователь может добавить товар в корзину")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "product_name",
        [
            "Sauce Labs Backpack",
            "Test.allTheThings() T-Shirt (Red)",
        ],
        ids=[
            "popular-product",
            "edge-case-product-name",
        ]
    )
    def test_user_can_add_product_to_cart(self, login, products_page, product_name):
        products_page.add_to_cart(product_name)
        assert products_page.get_cart_count() == 1

    @allure.story("Удаление товара")
    @allure.title("Пользователь может удалить товар из корзины со страницы товаров")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "product_name",
        [
            "Sauce Labs Backpack",
            "Test.allTheThings() T-Shirt (Red)",
        ],
        ids=[
            "popular-product",
            "edge-case-product-name",
        ]
    )
    def test_user_can_remove_product_from_products_page(self, login, products_page, product_name):
        products_page.add_to_cart(product_name)
        assert products_page.get_cart_count() == 1
        products_page.remove_from_cart(product_name)
        assert products_page.get_cart_count() == 0

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
    def test_user_can_sort_products_by_price(self, login, products_page, sort_value, reverse):
        products_page.sort_by(sort_value)
        prices = products_page.get_prices()
        assert prices == sorted(prices, reverse=reverse)

    @allure.story("Навигация")
    @allure.title("Пользователь может перейти в корзину")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_open_cart_from_products_page(self, login, products_page):
        products_page.click_open_cart()

        assert "cart" in products_page.driver.current_url

    @allure.story("Навигация")
    @allure.title("Пользователь может открыть карточку товара")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "product_name",
        [
            "Sauce Labs Backpack",
            "Test.allTheThings() T-Shirt (Red)",
        ],
        ids=[
            "popular-product",
            "edge-case-product-name",
        ]
    )
    def test_user_can_open_product_details(self, login, products_page, product_details_page, product_name):
        products_page.open_product_details(product_name)
        title = product_details_page.is_opened()
        assert title == product_name