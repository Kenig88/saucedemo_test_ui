from selenium.webdriver.support.ui import WebDriverWait  # правильный импорт
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple

Locator = Tuple[str, str]


class BasePage:
    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, timeout=10)

    def open(self) -> None:
        self.driver.get(self.url)

    def click(self, locator: Locator) -> None:  # для кликов по элементам (кнопки, текстовые поля)
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    # написать текст в текстовое поле
    def enter_text(self, locator: Locator, text: str, clear: bool = True) -> None:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        if clear:  # если clear true (по дефолту) то поле всегда будет предварительно очищаться, но если нужно просто дописать текст то нужно при вызове в аргументах писать false
            element.clear()
        element.send_keys(text)

    # получить текст
    def get_text(self, locator: Locator) -> str:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        text = element.text
        return text if text else element.get_attribute('value')  # Иногда .text может вернуть пустую строку (особенно если текст в value/input)

    # для ProductsPage и для других страниц если нужно что-то посчитать
    def get_elements_count(self, locator: Locator) -> int:
        elements = self.wait.until(EC.visibility_of_all_elements_located(locator))
        return len(elements)
