"""Фикстуры для тестов API"""

import pytest
import allure
from api.courier_api import CourierAPI
from api.orders_api import OrdersAPI
from helpers.data_generator import generate_courier_data


@pytest.fixture
def courier_data():
    """
    Фикстура для генерации данных курьера
    
    :return: словарь с данными курьера
    """
    return generate_courier_data()


@pytest.fixture
def created_courier():
    """
    Фикстура для создания курьера перед тестом и удаления после
    
    :return: tuple (courier_data, courier_id)
    """
    courier_data = generate_courier_data()
    
    # Создаем курьера
    response = CourierAPI.create_courier(courier_data)
    
    if response.status_code != 201:
        pytest.fail(f"Не удалось создать курьера для теста. Код: {response.status_code}")
    
    # Логинимся для получения ID
    login_response = CourierAPI.login_courier({
        "login": courier_data["login"],
        "password": courier_data["password"]
    })
    
    courier_id = None
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
    
    yield courier_data, courier_id
    
    # Удаляем курьера после теста
    if courier_id:
        with allure.step(f"Удаление тестового курьера ID: {courier_id}"):
            CourierAPI.delete_courier(courier_id)


@pytest.fixture
def created_order():
    """
    Фикстура для создания заказа перед тестом и отмены после
    
    :return: tuple (order_data, track_number)
    """
    from helpers.data_generator import generate_order_data
    
    order_data = generate_order_data(color=["BLACK"])
    
    # Создаем заказ
    response = OrdersAPI.create_order(order_data)
    
    track_number = None
    if response.status_code == 201:
        track_number = response.json().get("track")
    
    yield order_data, track_number
    
    # Отменяем заказ после теста (если он не был принят в работу)
    if track_number:
        with allure.step(f"Отмена тестового заказа track: {track_number}"):
            try:
                OrdersAPI.cancel_order(track_number)
            except:
                pass  # Игнорируем ошибки при удалении
