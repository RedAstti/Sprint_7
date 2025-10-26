# Sprint 7 - Автотесты API для Яндекс.Самокат

Автоматизация тестирования REST API сервиса аренды самокатов.

## 🛠 Технологии

- Python 3.10+
- Requests
- Pytest
- Allure

## 📁 Структура проекта

```
Sprint7/
├── api/                    # API клиенты
│   ├── courier_api.py      # Методы для работы с курьерами
│   └── orders_api.py       # Методы для работы с заказами
├── helpers/                # Вспомогательные функции
│   └── data_generator.py   # Генераторы тестовых данных
├── tests/                  # Тесты
│   ├── test_courier_create.py  # Тесты создания курьера
│   ├── test_courier_login.py   # Тесты авторизации курьера
│   ├── test_order_create.py    # Тесты создания заказа
│   └── test_order_list.py      # Тесты получения списка заказов
├── conftest.py            # Фикстуры pytest
├── urls.py                # URL константы
├── requirements.txt       # Зависимости
└── pytest.ini            # Настройки pytest
```

## 📦 Установка

1. Клонировать репозиторий
2. Создать виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate  # для macOS/Linux
venv\Scripts\activate     # для Windows
```

3. Установить зависимости:
```bash
pip install -r requirements.txt
```

## 🚀 Запуск тестов

### Запустить все тесты:
```bash
pytest tests/
```

### Запустить конкретный тестовый файл:
```bash
pytest tests/test_courier_create.py
```

### Запустить конкретный тестовый класс:
```bash
pytest tests/test_courier_create.py::TestCourierCreate
```

### Запустить конкретный тест:
```bash
pytest tests/test_courier_create.py::TestCourierCreate::test_create_courier_success
```

## 📊 Allure отчёт

### Сгенерировать отчёт:
```bash
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

## 🧪 Что тестируется

### 1. Создание курьера (`POST /api/v1/courier`)
- ✅ Успешное создание курьера
- ✅ Невозможность создания дубликата
- ✅ Валидация обязательных полей (login, password)
- ✅ Создание без необязательного поля firstName

### 2. Логин курьера (`POST /api/v1/courier/login`)
- ✅ Успешная авторизация
- ✅ Валидация обязательных полей
- ✅ Ошибка при неправильном логине/пароле
- ✅ Ошибка при несуществующем пользователе
- ✅ Возврат ID курьера

### 3. Создание заказа (`POST /api/v1/orders`)
- ✅ Создание с цветом BLACK
- ✅ Создание с цветом GREY
- ✅ Создание с обоими цветами
- ✅ Создание без указания цвета
- ✅ Возврат track номера

### 4. Список заказов (`GET /api/v1/orders`)
- ✅ Получение списка заказов
- ✅ Проверка структуры ответа
- ✅ Пагинация (limit, page)

## 📝 Примечания

- Все тесты независимы друг от друга
- Тестовые данные создаются перед тестом и удаляются после него
- Используется параметризация для тестирования различных вариантов цветов заказа
- Все запросы логируются в Allure отчёте

## 🔗 API Documentation

[https://qa-scooter.praktikum-services.ru/docs/](https://qa-scooter.praktikum-services.ru/docs/)
