from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.links import Links
import allure


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

    def __init__(self, driver):
        super().__init__(driver, url=Links.LOGIN_PAGE)

    def is_opened(self) -> bool:
        self.find(self.USERNAME)
        return self.driver.current_url == Links.LOGIN_PAGE

    def enter_username(self, username: str) -> None:
        self.enter_text(self.USERNAME, username)

    def enter_password(self, password: str) -> None:
        self.enter_text(self.PASSWORD, password)

    def click_login_button(self) -> None:
        self.click(self.LOGIN_BUTTON)

    def error_message_text(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def user_input(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
