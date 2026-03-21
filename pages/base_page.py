from selenium.webdriver.support.ui import WebDriverWait  # правильный импорт
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple
import allure

Locator = Tuple[str, str]


class BasePage:
    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, timeout=10)

    # для открытия первой страницы (LoginPage)
    def open(self) -> None:
        with allure.step(f"Открыть страницу: '{self.url}'."):
            self.driver.get(self.url)

    # проверка что страница открыта
    def assert_page_opened(self, url_part: str, title_page: Locator) -> str:
        with allure.step(f" Проверка что страница открыта."):
            element = self.wait.until(EC.visibility_of_element_located(title_page))
            current_url = self.driver.current_url
            assert url_part in current_url, f"Ожидал '{url_part}' в URL, получил '{current_url}'."
            return element.text

    # найти элемент
    def find(self, locator: Locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    # найти несколько элементов
    def find_all(self, locator: Locator):
        return self.driver.find_elements(*locator)

    def click(self, locator: Locator) -> None:  # для кликов по элементам (кнопки, текстовые поля)
        with allure.step(f"Клик по: '{locator}'."):
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()

    # ввод текста в текстовое поле
    def enter_text(self, locator: Locator, text: str, clear: bool = True) -> None:
        with allure.step(f"Ввод текста в поле: '{locator}'."):
            element = self.find(locator)
            if clear:  # если clear true (по дефолту) то поле всегда будет предварительно очищаться, но если нужно просто дописать текст то нужно при вызове в аргументах писать false
                element.clear()
            element.send_keys(text)

    # получить текст из локатора
    def get_text(self, locator: Locator) -> str:
        with allure.step(f"Получить текст из '{locator}'."):
            element = self.wait.find(locator)
            return element.text

    # для ProductsPage и для других страниц если нужно посчитать локаторы
    def get_elements_count(self, locator: Locator) -> int:
        with allure.step(f"Количество элементов в '{locator}'."):
            elements = self.find_all(locator)
            return len(elements)
