# 1-я часть дипломной работы: unit-тесты для сайта [StellarBurgers](https://stellarburgers.nomoreparties.site).

Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers.
Реализованные сценарии: 
- созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`;
- процент покрытия 100% (отчет: `htmlcov/index.html`)

## Технологии
- Python 3.10+
- [pytest](https://docs.pytest.org/)
- [pytest-cov](https://pypi.org/project/pytest-cov/)

## Структура проекта
```text
Diplom_1/
    ├── praktikum                    # Пакет, содержащщий код программы
    │   ├── bun.py       
    │   ├── burger.py
    │   ├── database.py
    │   ├── ingredient.py
    │   ├── ingredient_types.py
    │   ├── order_queue_page.py
    │ 
    ├── tests/                       # Тестовые сценарии
    │   ├── test_bun.py
    │   ├── test_burger.py
    │   ├── test_database.py
    │   ├── test_ingredient.py
    │   
    ├── conftest.py              # Файл с фикстурами
    ├── pytest.ini               # Конфигурационный файл
    └──  requirements.txt         # Файл с зависимостями для проекта
```

## Запуск автотестов

1. **Установка зависимостей**
> `$ pip install -r requirements.txt`

2. **Запуск автотестов и создание HTML-отчета о покрытии**
>  `$ pytest --cov=praktikum --cov-report=html`
