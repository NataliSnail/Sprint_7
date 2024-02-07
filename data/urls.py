
class TestBaseLinksAPI:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'


class TestCourierLinksAPI:
    LOGIN_URL = '/api/v1/courier/login'
    COURIER_URL = '/api/v1/courier/'
    COURIER_ORDER_URL = '/ordersCount'
    DELETE_COURIER_ID = '/api/v1/courier/:id'


class TestOrdersLinksAPI:
    MAIN_ORDERS_URL = '/api/v1/orders'
    TRACK_ORDER_URL = '/api/v1/orders/track?t='