"""Тесты для ручки POST /api/v1/courier/login - Логин курьера"""

import pytest
import allure
from api.courier_api import CourierAPI


@allure.suite("Логин курьера")
class TestCourierLogin:
    """Тесты для авторизации курьера"""

    @allure.title("Курьер может авторизоваться")
    @allure.description("Проверка успешной авторизации с валидными данными")
    def test_login_courier_success(self, created_courier):
        """Тест успешной авторизации курьера"""
        courier_data, courier_id = created_courier
        
        # Логинимся
        response = CourierAPI.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        
        # Проверяем код ответа
        assert response.status_code == 200, \
            f"Ожидался код 200, получен {response.status_code}"
        
        # Проверяем, что в ответе есть id
        response_data = response.json()
        assert "id" in response_data, \
            f"В ответе отсутствует поле 'id': {response_data}"
        assert response_data["id"] is not None, \
            "ID курьера не должен быть пустым"

    @allure.title("Авторизация без поля login")
    @allure.description("Проверка, что без login запрос возвращает ошибку 400")
    def test_login_without_login_fails(self, created_courier):
        """Тест авторизации без логина"""
        courier_data, _ = created_courier
        
        # Пытаемся залогиниться без login
        response = CourierAPI.login_courier({
            "password": courier_data["password"]
        })
        
        # Проверяем код ответа
        assert response.status_code == 400, \
            f"Ожидался код 400, получен {response.status_code}"
        
        # Проверяем сообщение об ошибке
        response_data = response.json()
        assert response_data.get("message") == "Недостаточно данных для входа", \
            f"Неверное сообщение об ошибке: {response_data}"

    @allure.title("Авторизация без поля password")
    @allure.description("Проверка, что без password запрос возвращает ошибку 400")
    def test_login_without_password_fails(self, created_courier):
        """Тест авторизации без пароля"""
        courier_data, _ = created_courier
        
        # Пытаемся залогиниться без password
        response = CourierAPI.login_courier({
            "login": courier_data["login"]
        })
        
        # Проверяем код ответа
        assert response.status_code == 400, \
            f"Ожидался код 400, получен {response.status_code}"
        
        # Проверяем сообщение об ошибке
        response_data = response.json()
        assert response_data.get("message") == "Недостаточно данных для входа", \
            f"Неверное сообщение об ошибке: {response_data}"

    @allure.title("Авторизация с неправильным логином")
    @allure.description("Проверка, что с несуществующим логином возвращается ошибка 404")
    def test_login_with_wrong_login_fails(self, created_courier):
        """Тест авторизации с неправильным логином"""
        courier_data, _ = created_courier
        
        # Пытаемся залогиниться с неправильным логином
        response = CourierAPI.login_courier({
            "login": "wronglogin123456",
            "password": courier_data["password"]
        })
        
        # Проверяем код ответа
        assert response.status_code == 404, \
            f"Ожидался код 404, получен {response.status_code}"
        
        # Проверяем сообщение об ошибке
        response_data = response.json()
        assert response_data.get("message") == "Учетная запись не найдена", \
            f"Неверное сообщение об ошибке: {response_data}"

    @allure.title("Авторизация с неправильным паролем")
    @allure.description("Проверка, что с неправильным паролем возвращается ошибка 404")
    def test_login_with_wrong_password_fails(self, created_courier):
        """Тест авторизации с неправильным паролем"""
        courier_data, _ = created_courier
        
        # Пытаемся залогиниться с неправильным паролем
        response = CourierAPI.login_courier({
            "login": courier_data["login"],
            "password": "wrongpassword123"
        })
        
        # Проверяем код ответа
        assert response.status_code == 404, \
            f"Ожидался код 404, получен {response.status_code}"
        
        # Проверяем сообщение об ошибке
        response_data = response.json()
        assert response_data.get("message") == "Учетная запись не найдена", \
            f"Неверное сообщение об ошибке: {response_data}"

    @allure.title("Авторизация под несуществующим пользователем")
    @allure.description("Проверка, что с несуществующими данными возвращается ошибка 404")
    def test_login_non_existent_user_fails(self):
        """Тест авторизации под несуществующим пользователем"""
        # Пытаемся залогиниться с полностью несуществующими данными
        response = CourierAPI.login_courier({
            "login": "nonexistentuser999",
            "password": "nonexistentpass999"
        })
        
        # Проверяем код ответа
        assert response.status_code == 404, \
            f"Ожидался код 404, получен {response.status_code}"
        
        # Проверяем сообщение об ошибке
        response_data = response.json()
        assert response_data.get("message") == "Учетная запись не найдена", \
            f"Неверное сообщение об ошибке: {response_data}"
