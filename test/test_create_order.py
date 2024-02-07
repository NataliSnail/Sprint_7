import allure
import pytest
import requests
from data.courier_api import *
from data.test_data import TestCourier, CourierErrors,TestOrder
from data.urls import TestBaseLinksAPI
from data.urls import TestCourierLinksAPI
from data.urls import TestOrdersLinksAPI
import random
from faker import Faker


class TestCreateOrderAPI:
    @allure.description('Проверка создания заказа с разными цветами | POST| MAIN_ORDERS_URL')
    @allure.title('Успешное создание заказа c разными цветами')
    @pytest.mark.parametrize('color', (["BLACK"], ["GREY"], ["BLACK", "GREY"], []))
    def test_create_order(self, color):
        TestOrder.test_order["color"] = [color]
        payload = json.dumps(TestOrder.test_order)
        response = requests.post(TestBaseLinksAPI.MAIN_URL + TestOrdersLinksAPI.MAIN_ORDERS_URL, data=payload)
        assert response.status_code == 201 and 'track' in response.text


    @allure.description('Проверка получения данных о заказе(трэк номера) | GET | TRACK_ORDER_URL')
    @allure.title('Успешное получение данных о заказе')
    def test_order_tracking_successful(self):
        new_track = return_new_order()
        payload = {"t": new_track}
        response = requests.get(TestBaseLinksAPI.MAIN_URL + TestOrdersLinksAPI.TRACK_ORDER_URL + str(new_track), data=payload)
        assert response.status_code == 200 and 'order' in response.text
