import pytest
from django.conf import settings
from rest_framework.test import APIClient

from ads.models import Ads, Feedback
from users.models import User


@pytest.fixture(scope="session", autouse=True)
def django_db_setup():
    """
    фикстура для создания тестовой БД
    :return:
    """
    # run_sql('DROP DATABASE IF EXISTS DW_test')
    # run_sql('CREATE DATABASE DW_test TEMPLATE DW')

    settings.DATABASES["default"] = {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "DW_test",
        "ATOMIC_REQUESTS": True,
    }


@pytest.fixture
def api_client():
    """
    Фикстура для создания экземпляра тестового API-клиента
    """
    return APIClient()


@pytest.fixture
def user():
    """
    Фикстура для создания экземпляра тестового пользователя
    """
    return User.objects.create(
        email="test1@mail.ru",
        role="user",
        password="1234",
    )


@pytest.fixture
def ads_db(user):
    """
    Фикстура для создания экземпляра тестового объявления
    """
    return Ads.objects.create(
        title="Test1",
        price=1000,
        author=user,
    )


@pytest.fixture
def feedback_db(user, ads_db):
    """
    Фикстура для создания экземпляра тестового отзыва
    """
    return Feedback.objects.create(
        text="Test1",
        ad=ads_db,
        author=user,
    )
