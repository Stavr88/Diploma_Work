import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import pytest
from django.conf import settings
from django.db import connections
from rest_framework.test import APIClient


from users.models import User
import requests


def run_sql(sql):
    conn = psycopg2.connect(database='postgres')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(sql)
    conn.close()


# @pytest.fixture
# def register_user():
#     """
#     Фикстура для регистрации пользователя
#     """
#     return User.objects.create(
#         email="test2@mail.ru",
#         password="1234",
#     )
#
#


# class APIClient:
#     @staticmethod
#     def login():
#         url = "http://127.0.0.1:8000/users/register/"
#         data = {"email": "test2@mail.ru", "password": "1234"}








@pytest.fixture(scope="session")
def django_db_setup():
    """
    фикстура для создания тестовой БД
    :return:
    """
    settings.DATABASES["default"] = {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "DW_test",
        "HOST": "127.0.0.1",
        "ATOMIC_REQUESTS": True,
    }
    run_sql('DROP DATABASE IF EXISTS the_copied_db')
    run_sql('CREATE DATABASE the_copied_db TEMPLATE the_source_db')

    yield

    for connection in connections.all():
        connection.close()

    run_sql('DROP DATABASE the_copied_db')


@pytest.fixture
class APIClient:
    @staticmethod
    def register_user(password, email):
        url = "http://127.0.0.1:8000/users/register/"
        data = {"email": "test2@mail.ru", "password": "1234"}
        response = requests.post(url, json=data)
        return response.json()


@pytest.fixture
def client():
    """Фикстура для создания экземпляра тестового API-клиента."""
    return APIClient()

