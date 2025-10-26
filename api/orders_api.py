"""API клиент для работы с заказами"""

import requests
import allure
from urls import ORDERS_CREATE, ORDERS_LIST, ORDERS_TRACK, ORDERS_CANCEL


class OrdersAPI:
    """Класс для работы с API заказов"""

    @staticmethod
    @allure.step("Создать заказ")
    def create_order(payload):
        """
        Создание нового заказа
        
        :param payload: данные заказа
        :return: response object
        """
        return requests.post(ORDERS_CREATE, json=payload)

    @staticmethod
    @allure.step("Получить список заказов")
    def get_orders_list(params=None):
        """
        Получение списка заказов
        
        :param params: параметры запроса (courierId, nearestStation, limit, page)
        :return: response object
        """
        return requests.get(ORDERS_LIST, params=params)

    @staticmethod
    @allure.step("Получить заказ по трек-номеру: {track_number}")
    def get_order_by_track(track_number):
        """
        Получение заказа по трекинговому номеру
        
        :param track_number: трекинговый номер заказа
        :return: response object
        """
        return requests.get(ORDERS_TRACK, params={"t": track_number})

    @staticmethod
    @allure.step("Отменить заказ с трек-номером: {track_number}")
    def cancel_order(track_number):
        """
        Отмена заказа
        
        :param track_number: трекинговый номер заказа
        :return: response object
        """
        return requests.put(ORDERS_CANCEL, json={"track": track_number})
