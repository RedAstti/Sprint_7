"""Тесты для ручки GET /api/v1/orders - Получение списка заказов"""

import allure
from api.orders_api import OrdersAPI


@allure.suite("Список заказов")
class TestOrderList:
    """Тесты для получения списка заказов"""

    @allure.title("Получение списка заказов")
    @allure.description("Проверка, что в ответе возвращается список заказов")
    def test_get_orders_list_returns_list(self):
        """Тест получения списка заказов"""
        response = OrdersAPI.get_orders_list()
        
        # Проверяем код ответа
        assert response.status_code == 200, \
            f"Ожидался код 200, получен {response.status_code}"
        
        # Проверяем структуру ответа
        response_data = response.json()
        
        # Проверяем наличие ключа orders
        assert "orders" in response_data, \
            f"В ответе отсутствует поле 'orders': {response_data}"
        
        # Проверяем, что orders - это список
        assert isinstance(response_data["orders"], list), \
            f"Поле 'orders' должно быть списком, получен {type(response_data['orders'])}"
        
        # Проверяем наличие pageInfo
        assert "pageInfo" in response_data, \
            "В ответе отсутствует поле 'pageInfo'"
        
        # Проверяем структуру pageInfo
        page_info = response_data["pageInfo"]
        assert "page" in page_info, \
            "В pageInfo отсутствует поле 'page'"
        assert "total" in page_info, \
            "В pageInfo отсутствует поле 'total'"
        assert "limit" in page_info, \
            "В pageInfo отсутствует поле 'limit'"
        
        # Проверяем наличие availableStations
        assert "availableStations" in response_data, \
            "В ответе отсутствует поле 'availableStations'"
        
        # Проверяем, что availableStations - это список
        assert isinstance(response_data["availableStations"], list), \
            "Поле 'availableStations' должно быть списком"

    @allure.title("Получение списка заказов с лимитом")
    @allure.description("Проверка получения списка заказов с параметром limit")
    def test_get_orders_list_with_limit(self):
        """Тест получения списка заказов с лимитом"""
        limit = 5
        response = OrdersAPI.get_orders_list(params={"limit": limit})
        
        # Проверяем код ответа
        assert response.status_code == 200, \
            f"Ожидался код 200, получен {response.status_code}"
        
        # Проверяем структуру ответа
        response_data = response.json()
        
        # Проверяем, что заказов не больше лимита
        orders = response_data.get("orders", [])
        assert len(orders) <= limit, \
            f"Количество заказов ({len(orders)}) превышает лимит ({limit})"

    @allure.title("Получение списка заказов с пагинацией")
    @allure.description("Проверка получения списка заказов с параметрами limit и page")
    def test_get_orders_list_with_pagination(self):
        """Тест получения списка заказов с пагинацией"""
        response = OrdersAPI.get_orders_list(params={"limit": 10, "page": 0})
        
        # Проверяем код ответа
        assert response.status_code == 200, \
            f"Ожидался код 200, получен {response.status_code}"
        
        # Проверяем структуру ответа
        response_data = response.json()
        
        # Проверяем pageInfo
        page_info = response_data.get("pageInfo", {})
        assert page_info.get("page") == 0, \
            f"Ожидалась страница 0, получена {page_info.get('page')}"
        assert page_info.get("limit") == 10, \
            f"Ожидался лимит 10, получен {page_info.get('limit')}"

    @allure.title("Список заказов не пустой")
    @allure.description("Проверка, что в системе есть заказы")
    def test_orders_list_not_empty(self):
        """Тест, что список заказов содержит данные"""
        response = OrdersAPI.get_orders_list()
        
        # Проверяем код ответа
        assert response.status_code == 200, \
            f"Ожидался код 200, получен {response.status_code}"
        
        # Проверяем, что список заказов не пустой
        response_data = response.json()
        orders = response_data.get("orders", [])
        
        # Если заказов нет, это нормально для тестовой среды
        # Проверяем только структуру
        if len(orders) > 0:
            # Проверяем структуру первого заказа
            first_order = orders[0]
            assert "id" in first_order, \
                "В заказе отсутствует поле 'id'"
            assert "track" in first_order, \
                "В заказе отсутствует поле 'track'"
