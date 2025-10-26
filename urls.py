"""URL константы для API Яндекс.Самокат"""

BASE_URL = "https://qa-scooter.praktikum-services.ru"

# Courier endpoints
COURIER_CREATE = f"{BASE_URL}/api/v1/courier"
COURIER_LOGIN = f"{BASE_URL}/api/v1/courier/login"
COURIER_DELETE = f"{BASE_URL}/api/v1/courier"  # + /:id

# Orders endpoints
ORDERS_CREATE = f"{BASE_URL}/api/v1/orders"
ORDERS_LIST = f"{BASE_URL}/api/v1/orders"
ORDERS_TRACK = f"{BASE_URL}/api/v1/orders/track"
ORDERS_ACCEPT = f"{BASE_URL}/api/v1/orders/accept"  # + /:id
ORDERS_FINISH = f"{BASE_URL}/api/v1/orders/finish"  # + /:id
ORDERS_CANCEL = f"{BASE_URL}/api/v1/orders/cancel"

# Utils endpoints
PING = f"{BASE_URL}/api/v1/ping"
STATIONS_SEARCH = f"{BASE_URL}/api/v1/stations/search"
