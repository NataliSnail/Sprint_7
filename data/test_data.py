import datetime
from datetime import date as d
import random
from faker import Faker


class TestCourier:
    only_password = {"password": "catcat"}
    empty_password = {"login": "tester", "password": ""}
    empty_login = {"login": "", "password": "catcat!"}

    non_existent_login_password = {"login": "ninja", "password": "1234"}

    create_no_login_courier = {"password": "catcat", "firstName": 'Ivan'}
    create_no_password_courier = {"login": "tester", "firstName": "Ivan"}
    create_empty_login = {"login": "", "password": "catcat", "firstName": "Ivan"}
    create_empty_password = {"login": "tester", "password": "", "firstName": "Ivan"}



class TestOrder:
    fake = Faker("ru_RU")
    test_order = {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": fake.address(),
            "metroStation": random.randint(0, 20),
            "phone": fake.phone_number(),
            "rentTime": random.randint(0, 24),
            "deliveryDate": fake.date(),
            "comment": fake.text(),
            "color": ["BLACK","Grey"]
        }

class CourierErrors:
    create_no_data = "Недостаточно данных для создания учетной записи"
    create_already_exist = "Этот логин уже используется. Попробуйте другой."

    login_no_data = "Недостаточно данных для входа"
    login_no_such_user = "Учетная запись не найдена"

