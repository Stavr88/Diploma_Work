from django.urls import path
from djoser.views import UserViewSet
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig


from users.views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name="register"),
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'), #Запрос токина для авторизации
    path("", UserListAPIView.as_view(permission_classes=(AllowAny,)), name="users_list"),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'), #Запрос для обновления токина "access"
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("resend-activation/", UserViewSet.as_view({"post": "resend_activation"}), name="resend_activation"), #Используйте эту конечную точку для повторной отправки электронного письма с активацией.
    path("activation/<str:uid>/<str:token>/", UserViewSet.as_view({"post": "activate"}), name="activate"),
    path("reset-password/", UserViewSet.as_view({"post": "reset_password"}), name="reset_password"),
    path(
        "reset-password-confirm/<str:uid>/<str:token>/",
        UserViewSet.as_view({"post": "reset_password_confirm"}),
        name="reset_password_confirm"
    ),
]
