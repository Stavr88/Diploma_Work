import pytest
from django.urls import reverse
from rest_framework import status

from ads.models import Ads, Feedback


@pytest.mark.django_db
def test_ads_create(user, api_client):
    """
    Тестирование создания объявления
    """
    api_client.force_authenticate(user=user)
    url = reverse("ads:ads_create")
    data = {
        "title": "Test1",
        "price": 1000,
        "author": user.id,
    }
    response = api_client.post(url, data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["title"] == "Test1"


@pytest.mark.django_db
def test_ads_list(user, api_client, ads_db):
    """
    Тестирование просмотра списка объявлений
    """
    api_client.force_authenticate(user=user)
    url = reverse("ads:ads_list")

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 1


@pytest.mark.django_db
def test_ads_retrieve(user, api_client, ads_db):
    """
    Тестирование просмотра одного объявления
    """
    api_client.force_authenticate(user=user)
    url = reverse("ads:ads_retrieve", args=(ads_db.id,))

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == "Test1"


@pytest.mark.django_db
def test_ads_update(user, api_client, ads_db):
    """
    Тестирование обновления объявления
    """
    api_client.force_authenticate(user=user)
    url = reverse("ads:ads_update", args=(ads_db.id,))
    data = {"title": "Test1"}

    response = api_client.patch(url, data)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == "Test1"


@pytest.mark.django_db
def test_ads_destroy(user, api_client, ads_db):
    """
    Тестирование удаления объявления
    """
    api_client.force_authenticate(user=user)
    url = reverse("ads:ads_destroy", args=(ads_db.id,))

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Ads.objects.filter(id=ads_db.id).exists() is False


@pytest.mark.django_db
def test_feedback_create(user, api_client, ads_db):
    """
    Тестирование создания отзыва
    """
    api_client.force_authenticate(user=user)
    url = reverse("ads:feedback_create")
    data = {
        "text": "Test111",
        "ad": ads_db.id,
        "author": user.id,
    }
    response = api_client.post(url, data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["ad"] == ads_db.id


@pytest.mark.django_db
def test_feedback_list(user, api_client, feedback_db):
    """
    Тестирование просмотра списка отзывов
    """
    api_client.force_authenticate(user=user)
    url = reverse("ads:feedback_list")

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


@pytest.mark.django_db
def test_feedback_retrieve(user, api_client, feedback_db):
    """
    Тестирование просмотра одного отзыва
    """
    api_client.force_authenticate(user=user)
    url = reverse("ads:feedback_retrieve", args=(feedback_db.id,))

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert Feedback.objects.filter(id=feedback_db.id).exists() is True


@pytest.mark.django_db
def test_feedback_update(user, api_client, feedback_db, ads_db):
    """
    Тестирование обновления отзыва
    """
    api_client.force_authenticate(user=user)
    url = reverse("ads:feedback_update", args=(feedback_db.id,))
    data = {"text": "Test1111", "ad": ads_db.id, "author": user.id}

    response = api_client.put(url, data)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["author"] == user.id


@pytest.mark.django_db
def test_feedback_destroy(user, api_client, feedback_db):
    """
    Тестирование удаления отзыва
    """
    api_client.force_authenticate(user=user)
    url = reverse("ads:feedback_destroy", args=(feedback_db.id,))

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Feedback.objects.count() == 0
