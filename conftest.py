from dotenv import load_dotenv
load_dotenv()  # Обычно load_dotenv() кладут не в data-файл, а в: 👉 conftest.py Так он выполняется один раз перед всеми тестами.

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import allure

from data.login_data import Username, Password


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browser_fixture")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="failed",
                attachment_type=allure.attachment_type.PNG
            )


# фикстура WebDriver'a
@pytest.fixture()
def browser_fixture():
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()


# фикстуры страниц
@pytest.fixture()
def login_page(browser_fixture):
    return LoginPage(browser_fixture)


@pytest.fixture()
def products_page(browser_fixture):
    return ProductsPage(browser_fixture)


# @pytest.fixture()
# def cart_page(browser_fixture):
#     return CartPage(browser_fixture)
#
#
# @pytest.fixture()
# def checkout_info_page(browser_fixture):
#     return CheckoutInfoPage(browser_fixture)
#
#
# @pytest.fixture()
# def checkout_overview_page(browser_fixture):
#     return CheckoutOverviewPage(browser_fixture)
#
#
# @pytest.fixture()
# def checkout_complete_page(browser_fixture):
#     return CheckoutCompletePage(browser_fixture)


# фикстура логина
@pytest.fixture()
def login(login_page):
    login_page.open()
    login_page.login(username=Username.STANDARD_USER, password=Password.SECRET_SAUCE)
