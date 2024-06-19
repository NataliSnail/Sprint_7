import allure
import pytest
import requests
from data.courier_api import *
from data.test_data import TestCourier, CourierErrors
from data.urls import TestBaseLinksAPI
from data.urls import TestCourierLinksAPI


class TestCourierCreateAPI:
    @allure.description('Проверка входа курьера по логину и паролю| POST | LOGIN_URL')
    @allure.title('Успешный вход курьера по логину и паролю')
    def test_successful_entrance_courier(self,test_user):
        login_courier = {"login": test_user[1][0],
                         "password": test_user[1][1]}
        response = requests.post(TestBaseLinksAPI.MAIN_URL + TestCourierLinksAPI.LOGIN_URL, data=login_courier)
        assert response.status_code == 200
        assert response.json()['id'] !=0


    @allure.description('Проверка входа курьера c незаполненными данными| POST | LOGIN_URL')
    @allure.title('Получение сообщения "Недостаточно данных для входа"')
    @pytest.mark.parametrize('user_data', (
    TestCourier.empty_login, TestCourier.empty_password, TestCourier.only_password))
    def test_entrance_with_empty_data(self,user_data):
        response = requests.post(TestBaseLinksAPI.MAIN_URL + TestCourierLinksAPI.LOGIN_URL, data=user_data)
        assert response.status_code == 400
        assert response.json()['message'] == CourierErrors.login_no_data

    @allure.description('Проверка входа курьера c несуществующими данными| POST |LOGIN_URL')
    @allure.title('Получение сообщения "Учетная запись не найдена"')
    def test_authorization_non_existent_data(self):
        login_courier = TestCourier.non_existent_login_password
        response = requests.post(TestBaseLinksAPI.MAIN_URL + TestCourierLinksAPI.LOGIN_URL, data=login_courier)
        assert response.status_code == 404
        assert response.json()['message'] == CourierErrors.login_no_such_user


    @allure.description('Проверка создания нового курьера| POST | LOGIN_URL')
    @allure.title('Успешное создание нового курьера')
    def test_create_new_courier_success(self, unregistered_user):
        response = requests.post(TestBaseLinksAPI.MAIN_URL + TestCourierLinksAPI.LOGIN_URL, data= unregistered_user)
        courier_id = response.json()["id"]
        requests.delete(TestBaseLinksAPI.MAIN_URL + TestCourierLinksAPI.LOGIN_URL + str(courier_id))
        assert response.status_code == 200


    @allure.description('Проверка создания нового курьера с незаполненными данными| POST | COURIER_URL')
    @allure.title('Получение сообщения "Недостаточно данных для создания учетной записи"')
    @pytest.mark.parametrize('user_data', (
            TestCourier.create_no_login_courier, TestCourier.create_no_password_courier, TestCourier.create_empty_login, TestCourier.create_empty_password))
    def test_create_new_courier_with_empty_data(self, user_data):
        response = requests.post(TestBaseLinksAPI.MAIN_URL + TestCourierLinksAPI.COURIER_URL, data=user_data)
        assert response.status_code == 400
        assert response.json()['message'] == CourierErrors.create_no_data

    @allure.description('Проверка создания нового курьера с одинаковым логином| POST | COURIER_URL')
    @allure.title('Получение сообщения "Этот логин уже используется. Попробуйте другой."')
    def test_create_new_courier_with_same_login(self, test_user):
        exist_login_courier = {
                "login": test_user[1][0],
                "password": test_user[1][1],
                "firstName": test_user[1][2]
            }
        response = requests.post(TestBaseLinksAPI.MAIN_URL + TestCourierLinksAPI.COURIER_URL, data=exist_login_courier)
        assert response.status_code == 409
        assert response.json()['message'] == CourierErrors.create_already_exist

    @allure.description('Проверка удаления созданного курьера по id| DELETE | DELETE_COURIER_ID')
    @allure.title('Успешное удаление данных по id"')
    def test_delete_courier_id(self, unregistered_user):
        response = requests.post(TestBaseLinksAPI.MAIN_URL + TestCourierLinksAPI.LOGIN_URL, data=unregistered_user)
        courier_id = response.json()["id"]
        requests.delete(TestBaseLinksAPI.MAIN_URL + TestCourierLinksAPI.DELETE_COURIER_ID + str(courier_id))
        assert response.status_code == 200
