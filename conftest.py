import pytest

from data.courier_api import *
from data.urls import TestBaseLinksAPI, TestCourierLinksAPI


@pytest.fixture()
def test_user():
    response, login_pass = register_new_courier_and_return_login_password()
    yield response, login_pass

    sign_in = {
    "login": login_pass[0],
    "password": login_pass[1]
    }

    courier_signin = requests.post(TestBaseLinksAPI.MAIN_URL + TestCourierLinksAPI.LOGIN_URL, data=sign_in)
    courier_id = courier_signin.json()["id"]
    requests.delete(TestBaseLinksAPI.MAIN_URL + TestCourierLinksAPI.LOGIN_URL + str(courier_id))



@pytest.fixture()
def unregistered_user():
    response, login_pass = register_new_courier_and_return_login_password()
    sign_in = {
    "login": login_pass[0],
    "password": login_pass[1]
    }
    return sign_in


