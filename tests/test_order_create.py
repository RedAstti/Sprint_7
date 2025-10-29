"""Тесты для ручки POST /api/v1/orders - Создание заказа"""

import pytest
import allure
from api.orders_api import OrdersAPI
from helpers.data_generator import generate_order_data


@allure.suite("Создание заказа")
class TestOrderCreate:
    """Тесты для создания заказа"""

    @allure.title("Создание заказа с цветом: {color}")
    @allure.description("Проверка создания заказа с различными вариантами цветов")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_colors(self, color, order_track_cleanup):
        """Тест создания заказа с разными цветами"""
        # Генерируем данные заказа
        order_data = generate_order_data(color=color if color else None)

        # Создаем заказ
        response = OrdersAPI.create_order(order_data)

        # Проверяем код ответа
        assert response.status_code == 201, \
            f"Ожидался код 201, получен {response.status_code}"

        # Проверяем, что в ответе есть track
        response_data = response.json()
        assert "track" in response_data, \
            f"В ответе отсутствует поле 'track': {response_data}"
        assert response_data["track"] is not None, \
            "Track номер не должен быть пустым"
        assert isinstance(response_data["track"], int), \
            f"Track должен быть числом, получен {type(response_data['track'])}"

        # Добавляем track в список для cleanup
        order_track_cleanup.append(response_data["track"])

    @allure.title("Создание заказа с одним цветом BLACK")
    @allure.description("Проверка создания заказа с цветом BLACK")
    def test_create_order_with_black_color(self, order_track_cleanup):
        """Тест создания заказа с черным цветом"""
        order_data = generate_order_data(color=["BLACK"])

        response = OrdersAPI.create_order(order_data)

        # Проверяем код ответа
        assert response.status_code == 201, \
            f"Ожидался код 201, получен {response.status_code}"

        # Проверяем track в ответе
        response_data = response.json()
        assert "track" in response_data, \
            "В ответе должен быть track номер"

        # Добавляем track в список для cleanup
        order_track_cleanup.append(response_data["track"])

    @allure.title("Создание заказа с одним цветом GREY")
    @allure.description("Проверка создания заказа с цветом GREY")
    def test_create_order_with_grey_color(self, order_track_cleanup):
        """Тест создания заказа с серым цветом"""
        order_data = generate_order_data(color=["GREY"])

        response = OrdersAPI.create_order(order_data)

        # Проверяем код ответа
        assert response.status_code == 201, \
            f"Ожидался код 201, получен {response.status_code}"

        # Проверяем track в ответе
        response_data = response.json()
        assert "track" in response_data, \
            "В ответе должен быть track номер"

        # Добавляем track в список для cleanup
        order_track_cleanup.append(response_data["track"])

    @allure.title("Создание заказа с обоими цветами")
    @allure.description("Проверка создания заказа с BLACK и GREY")
    def test_create_order_with_both_colors(self, order_track_cleanup):
        """Тест создания заказа с обоими цветами"""
        order_data = generate_order_data(color=["BLACK", "GREY"])

        response = OrdersAPI.create_order(order_data)

        # Проверяем код ответа
        assert response.status_code == 201, \
            f"Ожидался код 201, получен {response.status_code}"

        # Проверяем track в ответе
        response_data = response.json()
        assert "track" in response_data, \
            "В ответе должен быть track номер"

        # Добавляем track в список для cleanup
        order_track_cleanup.append(response_data["track"])

    @allure.title("Создание заказа без указания цвета")
    @allure.description("Проверка создания заказа без поля color")
    def test_create_order_without_color(self, order_track_cleanup):
        """Тест создания заказа без цвета"""
        order_data = generate_order_data(color=None)

        response = OrdersAPI.create_order(order_data)

        # Проверяем код ответа
        assert response.status_code == 201, \
            f"Ожидался код 201, получен {response.status_code}"

        # Проверяем track в ответе
        response_data = response.json()
        assert "track" in response_data, \
            "В ответе должен быть track номер"

        # Добавляем track в список для cleanup
        order_track_cleanup.append(response_data["track"])