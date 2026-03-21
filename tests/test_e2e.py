from time import sleep
import allure
import pytest


@allure.feature("E2E test.")
@pytest.mark.e2e
def test_checkout_flow(
        login,
        products_page,
        # добавляй по мере создания страниц
):
    sleep(1)

    # products_page

    title = products_page.is_opened()
    assert title == "Products"
    sleep(1)
    products_page.add_to_cart("Sauce Labs Backpack")
    assert products_page.get_cart_count() == 1
    sleep(1)
    products_page.click_open_cart()
    sleep(1)

    # cart_page


