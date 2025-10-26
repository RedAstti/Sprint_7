"""Тесты для ручки POST /api/v1/courier - Создание курьера"""

import pytest
import allure
from api.courier_api import CourierAPI
from helpers.data_generator import generate_courier_data


@allure.suite("Создание курьера")
class TestCourierCreate:
    """Тесты для создания курьера"""

    @allure.title("Курьера можно создать")
    @allure.description("Проверка успешного создания курьера с валидными данными")
    def test_create_courier_success(self, courier_data):
        """Тест успешного создания курьера"""
        response = CourierAPI.create_courier(courier_data)
        
        # Проверяем код ответа
        assert response.status_code == 201, \
            f"Ожидался код 201, получен {response.status_code}"
        
        # Проверяем тело ответа
        response_data = response.json()
        assert response_data.get("ok") is True, \
            f"Ожидалось 'ok': true, получено {response_data}"
        
        # Удаляем созданного курьера
        login_response = CourierAPI.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            CourierAPI.delete_courier(courier_id)

    @allure.title("Нельзя создать двух одинаковых курьеров")
    @allure.description("Проверка, что при попытке создать курьера с существующим логином возвращается ошибка 409")
    def test_create_duplicate_courier_fails(self, created_courier):
        """Тест создания дубликата курьера"""
        courier_data, courier_id = created_courier
        
        # Пытаемся создать курьера с тем же логином
        response = CourierAPI.create_courier(courier_data)
        
        # Проверяем код ответа
        assert response.status_code == 409, \
            f"Ожидался код 409 (Conflict), получен {response.status_code}"
        
        # Проверяем сообщение об ошибке
        response_data = response.json()
        assert "Этот логин уже используется" in response_data.get("message"), \
            f"Неверное сообщение об ошибке: {response_data}"

    @allure.title("Создание курьера без обязательного поля login")
    @allure.description("Проверка, что без поля login запрос возвращает ошибку 400")
    def test_create_courier_without_login_fails(self, courier_data):
        """Тест создания курьера без логина"""
        # Удаляем поле login
        del courier_data["login"]
        
        response = CourierAPI.create_courier(courier_data)
        
        # Проверяем код ответа
        assert response.status_code == 400, \
            f"Ожидался код 400, получен {response.status_code}"
        
        # Проверяем сообщение об ошибке
        response_data = response.json()
        assert response_data.get("message") == "Недостаточно данных для создания учетной записи", \
            f"Неверное сообщение об ошибке: {response_data}"

    @allure.title("Создание курьера без обязательного поля password")
    @allure.description("Проверка, что без поля password запрос возвращает ошибку 400")
    def test_create_courier_without_password_fails(self, courier_data):
        """Тест создания курьера без пароля"""
        # Удаляем поле password
        del courier_data["password"]
        
        response = CourierAPI.create_courier(courier_data)
        
        # Проверяем код ответа
        assert response.status_code == 400, \
            f"Ожидался код 400, получен {response.status_code}"
        
        # Проверяем сообщение об ошибке
        response_data = response.json()
        assert response_data.get("message") == "Недостаточно данных для создания учетной записи", \
            f"Неверное сообщение об ошибке: {response_data}"

    @allure.title("Создание курьера без обоих обязательных полей")
    @allure.description("Проверка, что без login и password запрос возвращает ошибку 400")
    def test_create_courier_without_required_fields_fails(self):
        """Тест создания курьера без обязательных полей"""
        # Создаем курьера только с firstName
        courier_data = {"firstName": "Test"}
        
        response = CourierAPI.create_courier(courier_data)
        
        # Проверяем код ответа
        assert response.status_code == 400, \
            f"Ожидался код 400, получен {response.status_code}"
        
        # Проверяем сообщение об ошибке
        response_data = response.json()
        assert response_data.get("message") == "Недостаточно данных для создания учетной записи", \
            f"Неверное сообщение об ошибке: {response_data}"

    @allure.title("Можно создать курьера без поля firstName")
    @allure.description("Проверка, что курьера можно создать только с login и password")
    def test_create_courier_without_first_name_success(self, courier_data):
        """Тест создания курьера без имени"""
        # Удаляем необязательное поле firstName
        del courier_data["firstName"]
        
        response = CourierAPI.create_courier(courier_data)
        
        # Проверяем код ответа
        assert response.status_code == 201, \
            f"Ожидался код 201, получен {response.status_code}"
        
        # Проверяем тело ответа
        response_data = response.json()
        assert response_data.get("ok") is True, \
            f"Ожидалось 'ok': true, получено {response_data}"
        
        # Удаляем созданного курьера
        login_response = CourierAPI.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            CourierAPI.delete_courier(courier_id)
