import allure
import pytest
import requests
from data.courier_api import *
from data.urls import TestBaseLinksAPI
from data.urls import TestOrdersLinksAPI

class TestOrdersListAPI:
    @allure.description('Проверить получение списка заказов| GET /api/v1/orders')
    @allure.title('Успешное получение списка заказов')
    def test_check_orders_list(self):
        response = requests.get(TestBaseLinksAPI.MAIN_URL + TestOrdersLinksAPI.MAIN_ORDERS_URL)
        orders_list = response.json()["orders"]
        assert response.status_code == 200
        assert isinstance(orders_list, list) == True
