# <p align="center"> 🛒 SauceDemo UI Test Automation </p>

Проект автоматизации UI-тестирования, построенный с использованием:

🐍 Python + Pytest 

🌐 Selenium WebDriver 

🐳 Docker + Docker Compose 

📊 Allure Report  + GitHub Actions CI

---

# <p align="center"> - Описание проекта - </p>

Этот проект демонстрирует полноценный UI тестовый фреймворк, включающий:

- Page Object Model (POM) архитектуру  
- Разделение тестов, страниц и данных  
- Фикстуры для управления браузером  
- Allure-отчёты со скриншотами при падении  
- Параллельный запуск тестов  
- Docker-исполнение  
- CI с публикацией отчётов  

В качестве тестового окружения используется сайт SauceDemo.

---

# <p align="center"> - Структура проекта - </p>

```text
saucedemo_test_ui/              # Корневая папка проекта
│
├── pages/                      # Page Object слой (логика страниц)
├── tests/                      # UI тесты (test cases)
├── config/                       # Тестовые данные (логины, товары, checkout)
│
├── conftest.py                 # Фикстуры (driver, hooks, setup/teardown)
├── pytest.ini                  # Конфигурация pytest
├── requirements.txt            # Зависимости проекта
│
├── Dockerfile                  # Docker образ для запуска тестов
├── docker-compose.yml          # Docker orchestration
│
├── .env.example                # Пример переменных окружения
└── README.md                   # Документация проекта
```

---

# <p align="center"> - Переменные окружения - </p>

Создайте файл .env на основе .env.example:

```text
STANDARD_USER = "___write___your___data___"
LOCKED_OUT_USER = "___write___your___data___"
PROBLEM_USER = "___write___your___data___"
PERFORMANCE_GLITCH_USER = "___write___your___data___"
ERROR_USER = "___write___your___data___"
VISUAL_USER = "___write___your___data___"
INVALID_LOGIN = "___write___your___data___"

SECRET_SAUCE = "___write___your___data___"
INVALID_PASSWORD = "___write___your___data___"
```

---

# <p align="center"> 🐳 Локальный запуск тестов (через Docker). </p>

Запуск всех тестов: 

```bash
docker compose run --rm all
```

Запуск отдельных наборов тестов:

```bash

docker compose run --rm e2e
docker compose run --rm regression
```

---

# <p align="center"> 🧪 Локальный запуск без Docker. </p>

Установка зависимостей:

```bash
pip install -r requirements.txt
```

Запуск тестов (пример):

```bash
pytest -v tests/test_login_page.py 
```

Параллельный запуск (пример):

```bash
pytest tests/test_products_page.py -n 2
```

---

# <p align="center"> 📊 Генерация Allure-отчёта локально. </p>

После выполнения тестов:

```bash
pytest --alluredir=allure-results
```

Генерация отчёта:

```bash
allure generate allure-results -o allure-report --clean
```

Запуск:

```bash
allure serve allure-results
```

---

# <p align="center"> 📸 Скриншоты при падении. </p>

При падении теста автоматически:

* Делается скриншот
* Прикрепляется к Allure отчёту

---

# <p align="center"> 🧠 Особенности фреймворка. </p>

🔹 Page Object Model (POM):

Чистое разделение логики страниц и тестов.

🔹 Разделение данных:

Все тестовые данные вынесены в data/.

🔹 Чистые тесты:

Тесты описывают только пользовательские сценарии.

🔹 Фикстуры pytest:

Централизованное управление драйвером и тестами.

🔹 Параллельный запуск:

Поддержка pytest-xdist.

🔹 Docker:

Одинаковое выполнение тестов в любом окружении.

---

# <p align="center"> 🧪 Покрываемые сценарии. </p>

* Авторизация
* Просмотр товаров
* Добавление в корзину
* Checkout flow

---

# <p align="center"> 🚀 CI: GitHub Actions + Allure + Pages. </p>

Проект включает CI-пайплайн с автоматическим запуском тестов и публикацией отчётов.

Возможности CI:

* Ручной запуск workflow
* Запуск тестов в Docker / Python окружении
* Генерация Allure HTML отчёта
* Публикация в GitHub Pages
* Сохранение истории запусков (Trend graph)

---

# <p align="center"> ▶ Как запустить CI. </p>

1. Перейдите в GitHub → Actions
2. Выберите workflow:

```text
UI Tests + Allure Report
```

3. Нажмите Run workflow
4. Запустите выполнение

---

# <p align="center"> 🌐 Онлайн-отчёт Allure. </p>

После запуска CI отчёт доступен по адресу:

```text
https://kenig88.github.io/test_selenium_saucedemo/
```

---

# <p align="center"> 📈 История запусков (Allure Trend). </p>

1. Откройте отчёт
2. Перейдите в:

```text
Graphs → Trend
```

3. Посмотрите динамику выполнения тестов

---

# <p align="center"> 🔒 Безопасность. </p>

* .env исключён через .gitignore
* Нет использования продакшн-данных
* Переменные через environment

---

# <p align="center"> 🏆 Что демонстрирует проект. </p>

* UI automation (Selenium + Pytest)
* Page Object Model
* Allure отчёты
* Docker запуск
* CI/CD интеграцию
* GitHub Pages публикацию
* Историю запусков тестов

---

# <p align="center"> 📈 Возможные улучшения. </p>

* Разделение тестов на smoke / regression
* Retry механизм
* Selenium Grid / Selenoid
* Логирование

---