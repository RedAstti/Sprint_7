"""Генераторы тестовых данных"""

import random
import string


def generate_random_string(length=10):
    """
    Генерирует случайную строку из букв нижнего регистра
    
    :param length: длина строки
    :return: случайная строка
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_courier_data():
    """
    Генерирует данные для создания курьера
    
    :return: словарь с login, password, firstName
    """
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }


def generate_order_data(color=None):
    """
    Генерирует данные для создания заказа
    
    :param color: список цветов ["BLACK", "GREY"] или None
    :return: словарь с данными заказа
    """
    order_data = {
        "firstName": generate_random_string(8),
        "lastName": generate_random_string(8),
        "address": f"{generate_random_string(10)}, {random.randint(1, 200)} apt.",
        "metroStation": str(random.randint(1, 237)),
        "phone": f"+7{random.randint(1000000000, 9999999999)}",
        "rentTime": random.randint(1, 7),
        "deliveryDate": "2024-12-31",
        "comment": generate_random_string(15)
    }
    
    if color is not None:
        order_data["color"] = color
    
    return order_data
