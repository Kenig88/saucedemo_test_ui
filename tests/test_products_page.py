import pytest
import allure


@allure.feature("Test Products Page.")
@pytest.mark.regression
class TestProductsRegression:

    # ✅ 1. Проверка открытия страницы
    @allure.feature("Страница товаров.")
    @allure.title("Проверка успешного открытия страницы товаров.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_products_page_opened(self, login, products_page):
        title = products_page.is_opened()
        # is_opened():
        # - проверяет что URL содержит "inventory"
        # - проверяет что заголовок виден
        # - возвращает текст заголовка

        assert title == "Products"
        # убеждаемся что открылась именно нужная страница

    # ✅ 2. Проверка количества товара на странице
    @allure.story("Отображение товаров.")
    @allure.title("Проверка количества товаров на странице.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_products_count(self, login, products_page):
        count = products_page.get_products_count()
        # метод считает количество карточек товаров на странице

        assert count == 6
        # проверяем что товаров ровно 6 (в saucedemo)

    # ✅ 3. Добавление товара в корзину
    @allure.story("Добавление в корзину.")
    @allure.title("Добавление одного товара в корзину.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("product_name", [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
    ])
    def test_add_product_to_cart(self, login, products_page, product_name):
        allure.dynamic.parameter("Товар: ", product_name)

        # pytest запустит тест 2 раза с разными товарами

        products_page.add_to_cart(product_name)
        # нажимаем кнопку Add to cart у конкретного товара

        assert products_page.get_cart_count() == 1
        # проверяем что счетчик корзины стал 1

    # ✅ 4. Добавление нескольких товаров
    @allure.story("Добавление нескольких товаров.")
    @allure.title("Добавление нескольких товаров в корзину.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("products, expected", [
        (["Sauce Labs Backpack", "Sauce Labs Bike Light"], 2),
        (["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"], 3)
    ])
    def test_add_multiple_products(self, login, products_page, products, expected):
        allure.dynamic.parameter("Товары: ", products)

        # products → список товаров
        # expected → сколько должно быть в корзине

        for product in products:
            products_page.add_to_cart(product)
            # добавляем каждый товар по очереди

        assert products_page.get_cart_count() == expected
        # проверяем итоговое количество

    # ✅ 5. Удаление товара
    @allure.story("Удаление товара.")
    @allure.title("Удаление товара из корзины.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("product_name", [
        "Sauce Labs Backpack",
        "Test.allTheThings() T-Shirt (Red)"
    ])
    def test_remove_product(self, login, products_page, product_name):
        allure.dynamic.parameter("Товар: ", product_name)

        # сначала добавляем товар
        products_page.add_to_cart(product_name)
        assert products_page.get_cart_count() == 1

        # потом нажимаем ту же кнопку → она превращается в "Remove"
        products_page.add_to_cart(product_name)

        assert products_page.get_cart_count() == 0
        # корзина должна стать пустой (бейдж исчезает)

    # ✅ 6. Сортировка
    @allure.story("Сортировка товаров.")
    @allure.title("Проверка сортировки товаров.")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("sort_value, reverse", [
        ("lohi", False),  # low → high
        ("hilo", True)  # high → low
    ])
    def test_sort_products(self, login, products_page, sort_value, reverse):
        allure.dynamic.parameter("Тип сортировки: ", sort_value)

        products_page.sort_by(sort_value)
        # выбираем сортировку из dropdown

        prices = products_page.get_prices()
        # получаем список цен со страницы

        assert prices == sorted(prices, reverse=reverse)
        # сравниваем с "правильной" сортировкой Python

    # ✅ 7. Переход в корзину
    @allure.story("Навигация.")
    @allure.title("Переход на страницу корзины.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_cart_page(self, login, products_page, browser_fixture):
        products_page.click_open_cart()
        # кликаем на иконку корзины

        assert "cart" in browser_fixture.current_url
        # проверяем что URL изменился → мы на странице корзины

    # ✅ 8. Переход в карточку товара
    @allure.story("Карточка товара.")
    @allure.title("Переход на страницу товара.")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("product_name", [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
    ])
    def test_open_product_detail(self, login, products_page, product_name):
        allure.dynamic.parameter("Товар: ", product_name)

        products_page.click_open_product(product_name)
        # кликаем по названию товара

        assert "inventory-item" in products_page.driver.current_url
        # проверяем что открылась страница товара
