from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import User


class UserSerializer(ModelSerializer):
    """
    Сериализатор для модели User
    """

    class Meta:
        model = User
        fields = ("email", "first_name", "last_login", "id", "is_active", "country")


