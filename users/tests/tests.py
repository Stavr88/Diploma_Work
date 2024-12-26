
from rest_framework.test import APITestCase
import pytest
from django.urls import reverse
from rest_framework import status
from users.models import User


# class UserTestCase(APITestCase):
#
#     def test_user_create(self):
#         url = reverse("users:register")
#         data = {
#             "email": "test2@mail.ru",
#             "password": "1234",
#         }
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(User.objects.all().count(), 1)

# @pytest.mark.django_db
# def test_user_create(register_user):
#     """
#     Тестирование создания пользователя
#     """
#     url = reverse("users:register")
#     data = {
#         "email": "test2@mail.ru",
#         "password": "1234",
#     }
#     response = register_user.post(url, data)
#
#     assert response.status_code == status.HTTP_201_CREATED
#     assert response.data["email"] == "test2@mail.ru"
#
#
# def test_registration_successful(APIClient):
#     password = "new_password"
#     email = "new_user@example.com"
#
#     # Отправка запроса на регистрацию пользователя
#     response = APIClient.register_user(password, email)
#
#     # Проверки успешной регистрации
#     assert response["status"] == "success"
#     assert response["message"] == "User registered successfully"
#
#


@pytest.mark.django_db
def test_user_create(client):
    """Тестирование создания пользователя."""
    url = reverse("users:register")
    data = {
        "email": "user@test.com",
        "first_name": "test_first",
        "last_name": "test_last",
        "role": "user",
        "password": "123teST",
    }
    response = client.post(url, data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["email"] == "user@test.com"
