import requests
import random
import string
import json
from data.test_data import TestOrder
from data.urls import TestBaseLinksAPI, TestCourierLinksAPI, TestOrdersLinksAPI


def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(TestBaseLinksAPI.MAIN_URL + TestCourierLinksAPI.COURIER_URL, data=payload)
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return response, login_pass

def return_new_order():
    payload = json.dumps(TestOrder.test_order)
    response = requests.post(TestBaseLinksAPI.MAIN_URL + TestOrdersLinksAPI.MAIN_ORDERS_URL, data=payload)
    track = response.json()["track"]
    return track
