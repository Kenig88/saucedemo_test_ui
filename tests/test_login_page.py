import pytest
import allure

from data.login_data import Username, Password, ErrorMessages
from data.links import Links


@allure.feature("Login Page")
@pytest.mark.regression
class TestLoginPage:

    @allure.story("Успешный логин")
    @allure.title("Пользователь может войти с валидными credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_login_with_valid_credentials(self, login_page):
        login_page.open()
        login_page.is_opened()
        login_page.user_input(Username.STANDARD_USER, Password.SECRET_SAUCE)
        assert "inventory" in login_page.driver.current_url

    @allure.story("Валидация формы")
    @allure.title("Пользователь видит ошибки при пустых обязательных полях")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "username, password, expected_error",
        [
            (None, Password.SECRET_SAUCE, ErrorMessages.EMPTY_USERNAME),
            (Username.STANDARD_USER, None, ErrorMessages.EMPTY_PASSWORD),
        ],
        ids=[
            "empty-username",
            "empty-password",
        ]
    )
    def test_user_sees_error_with_empty_fields(
        self, login_page, username, password, expected_error
    ):
        login_page.open()
        login_page.is_opened()
        if username:
            login_page.enter_username(username)
        if password:
            login_page.enter_password(password)
        login_page.click_login_button()
        assert login_page.driver.current_url == Links.LOGIN_PAGE
        assert login_page.error_message_text() == expected_error

    @allure.story("Невалидный логин")
    @allure.title("Пользователь видит ошибку при неуспешной попытке входа")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "username, password, expected_error",
        [
            (Username.STANDARD_USER, Password.INVALID_PASSWORD, ErrorMessages.INCORRECT_DATA),
            (Username.LOCKED_OUT_USER, Password.SECRET_SAUCE, ErrorMessages.BLOCKED_USER),
        ],
        ids=[
            "invalid-password",
            "locked-out-user",
        ]
    )
    def test_user_sees_error_when_login_fails(
        self, login_page, username, password, expected_error
    ):
        login_page.open()
        login_page.is_opened()
        login_page.user_input(username, password)
        assert login_page.driver.current_url == Links.LOGIN_PAGE
        assert login_page.error_message_text() == expected_error

    @allure.story("Повторная попытка логина")
    @allure.title("Пользователь может успешно войти после предыдущей неудачной попытки")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_login_after_previous_failed_attempt(self, login_page):
        login_page.open()
        login_page.is_opened()
        login_page.user_input(Username.STANDARD_USER, Password.INVALID_PASSWORD)
        assert login_page.driver.current_url == Links.LOGIN_PAGE
        assert login_page.error_message_text() == ErrorMessages.INCORRECT_DATA
        login_page.user_input(Username.STANDARD_USER, Password.SECRET_SAUCE)
        assert "inventory" in login_page.driver.current_url