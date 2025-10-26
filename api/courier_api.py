"""API клиент для работы с курьерами"""

import requests
import allure
from urls import COURIER_CREATE, COURIER_LOGIN, COURIER_DELETE


class CourierAPI:
    """Класс для работы с API курьеров"""

    @staticmethod
    @allure.step("Создать курьера")
    def create_courier(payload):
        """
        Создание нового курьера
        
        :param payload: данные курьера (login, password, firstName)
        :return: response object
        """
        return requests.post(COURIER_CREATE, json=payload)

    @staticmethod
    @allure.step("Логин курьера")
    def login_courier(payload):
        """
        Авторизация курьера
        
        :param payload: данные для входа (login, password)
        :return: response object
        """
        return requests.post(COURIER_LOGIN, json=payload, timeout=10)

    @staticmethod
    @allure.step("Удалить курьера с ID: {courier_id}")
    def delete_courier(courier_id):
        """
        Удаление курьера по ID
        
        :param courier_id: ID курьера
        :return: response object
        """
        return requests.delete(f"{COURIER_DELETE}/{courier_id}")
