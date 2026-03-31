from typing import Tuple
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Locator = Tuple[str, str]


class BasePage:
    def __init__(self, driver, url: str, timeout: int = 10):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, timeout)

    # --- Navigation (навигация по страницам) ---

    def open(self) -> None:
        """
        Открыть страницу по URL, заданному в Page Object.
        Используется для стартовой страницы (LoginPage).
        """
        self.driver.get(self.url)

    # --- Page state (проверка состояния страницы) ---

    def assert_page_opened(self, url_part: str, title_locator: Locator) -> str:
        """
        Проверяю, что открыта нужная страница:
        - URL содержит ожидаемую часть
        - ключевой элемент (заголовок) видим

        Метод возвращает текст заголовка.
        """
        element = self.find(title_locator)
        current_url = self.driver.current_url
        assert url_part in current_url, f"Ожидал '{url_part}' в URL, получил '{current_url}'."
        return element.text

    # --- Find elements (поиск элементов) ---

    def find(self, locator: Locator):
        """
        Найти один элемент с ожиданием (visibility).
        Основной метод для работы с элементами.
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator: Locator):
        """
        Найти список элементов без ожидания.
        Используется, когда элемент может отсутствовать.
        """
        return self.driver.find_elements(*locator)

    # --- Actions (действия пользователя) ---

    def click(self, locator: Locator) -> None:
        """
        Клик по элементу с ожиданием, что он кликабельный.
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator: Locator, text: str, clear: bool = True) -> None:
        """
        Ввод текста в поле:
        - по умолчанию очищает поле перед вводом
        - можно отключить очистку (clear=False)
        """
        element = self.find(locator)
        if clear:
            element.clear()
        element.send_keys(text)

    # --- Get config (получение данных из UI) ---

    def get_text(self, locator: Locator) -> str:
        """
        Получить текст элемента.
        """
        return self.find(locator).text

    def get_elements_count(self, locator: Locator) -> int:
        """
        Получить количество элементов (например, товаров на странице).
        """
        return len(self.find_all(locator))
