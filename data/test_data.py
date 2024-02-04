import datetime
from datetime import date as d


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
    test_order = {"order":
{
    "firstName": "Harry",
    "lastName": "Potter",
    "address": "Privet drive, 4 ",
    "metroStation": 4,
    "phone": "+7 999 888 77 66",
    "rentTime": 5,
    "deliveryDate": "2022-02-22",
    "comment": "test comment",
    "color": ["BLACK"]
 }
    }


class CourierErrors:
    create_no_data = "Недостаточно данных для создания учетной записи"
    create_already_exist = "Этот логин уже используется. Попробуйте другой."

    login_no_data = "Недостаточно данных для входа"
    login_no_such_user = "Учетная запись не найдена"

