from dotenv import load_dotenv

load_dotenv()  # Загружает переменные окружения перед запуском всех тестов

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import allure

from data.login_data import Username, Password
from data.products_data import ProductNames
from data.checkout_data import CheckoutInfoData


# Хук для прикрепления скриншота при падении теста (усилил для xdist)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browser_fixture")
        if driver:
            worker_id = "master"
            if hasattr(item.config, "workerinput"):
                worker_id = item.config.workerinput.get("workerid", "worker")

            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"failed-{worker_id}",
                attachment_type=allure.attachment_type.PNG
            )


# Создаёт и закрывает WebDriver для каждого теста
@pytest.fixture()
def browser_fixture():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--window-size=1920,1080")

    # Раскомментировать для Docker и CI:
    # options.add_argument("--headless=new")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(20)

    yield driver
    driver.quit()


# Возвращает PageObject страницы логина
@pytest.fixture()
def login_page(browser_fixture):
    return LoginPage(browser_fixture)


# Возвращает PageObject страницы товаров
@pytest.fixture()
def products_page(browser_fixture):
    return ProductsPage(browser_fixture)


# Возвращает PageObject страницы деталей товара
@pytest.fixture()
def product_details_page(browser_fixture):
    return ProductDetailsPage(browser_fixture)


# Возвращает PageObject страницы корзины
@pytest.fixture()
def cart_page(browser_fixture):
    return CartPage(browser_fixture)


# Возвращает PageObject страницы checkout (шаг 1)
@pytest.fixture()
def checkout_info_page(browser_fixture):
    return CheckoutInfoPage(browser_fixture)


# Возвращает PageObject страницы checkout (шаг 2)
@pytest.fixture()
def checkout_overview_page(browser_fixture):
    return CheckoutOverviewPage(browser_fixture)


# Возвращает PageObject страницы успешного завершения заказа
@pytest.fixture()
def checkout_complete_page(browser_fixture):
    return CheckoutCompletePage(browser_fixture)


# Выполняет логин пользователя
@pytest.fixture()
def login(login_page):
    login_page.open()
    login_page.user_input(username=Username.STANDARD_USER, password=Password.SECRET_SAUCE)


# Открывает корзину после логина (без добавления товара)
@pytest.fixture()
def opened_cart_page(login_page, products_page, cart_page):
    login_page.open()
    login_page.user_input(
        username=Username.STANDARD_USER,
        password=Password.SECRET_SAUCE
    )
    products_page.click_open_cart()
    return cart_page


# Открывает корзину с добавленным товаром
@pytest.fixture()
def opened_cart_page_with_product(login_page, products_page, cart_page):
    def _open(product_name: str):
        login_page.open()
        login_page.user_input(
            username=Username.STANDARD_USER,
            password=Password.SECRET_SAUCE
        )
        products_page.add_to_cart(product_name)
        products_page.click_open_cart()
        return cart_page

    return _open


# Открывает checkout step one (после корзины)
@pytest.fixture()
def opened_checkout_info_page(login_page, products_page, cart_page, checkout_info_page):
    login_page.open()
    login_page.user_input(
        username=Username.STANDARD_USER,
        password=Password.SECRET_SAUCE
    )
    products_page.add_to_cart(ProductNames.BACKPACK)
    products_page.click_open_cart()
    cart_page.click_checkout()
    return checkout_info_page


# Открывает checkout overview (после заполнения данных)
@pytest.fixture()
def opened_checkout_overview_page(
    login_page,
    products_page,
    cart_page,
    checkout_info_page,
    checkout_overview_page,
):
    login_page.open()
    login_page.user_input(
        username=Username.STANDARD_USER,
        password=Password.SECRET_SAUCE
    )
    products_page.add_to_cart(ProductNames.BACKPACK)
    products_page.click_open_cart()
    cart_page.click_checkout()
    checkout_info_page.fill_checkout_form(
        CheckoutInfoData.FIRST_NAME,
        CheckoutInfoData.LAST_NAME,
        CheckoutInfoData.POSTAL_CODE,
    )
    checkout_info_page.click_continue_button()
    return checkout_overview_page


# Открывает страницу успешного завершения заказа (после finish)
@pytest.fixture()
def opened_checkout_complete_page(
    login_page,
    products_page,
    cart_page,
    checkout_info_page,
    checkout_overview_page,
    checkout_complete_page,
):
    login_page.open()
    login_page.user_input(
        username=Username.STANDARD_USER,
        password=Password.SECRET_SAUCE
    )
    products_page.add_to_cart(ProductNames.BACKPACK)
    products_page.click_open_cart()
    cart_page.click_checkout()
    checkout_info_page.fill_checkout_form(
        CheckoutInfoData.FIRST_NAME,
        CheckoutInfoData.LAST_NAME,
        CheckoutInfoData.POSTAL_CODE,
    )
    checkout_info_page.click_continue_button()
    checkout_overview_page.click_finish()
    return checkout_complete_page