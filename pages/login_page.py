from pages.base_page import BasePage
from data.links import Links


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, Links.LOGIN_PAGE)