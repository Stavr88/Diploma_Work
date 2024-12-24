from django.urls import path, include, re_path
from djoser.views import UserViewSet
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from rest_framework.routers import SimpleRouter

from users.views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = UsersConfig.name

# router = SimpleRouter()
# router.register('', PaymentViewSet, basename='payment')

# urlpatterns = [
#     path('register/', UserCreateAPIView.as_view(), name='register'),
#     path('view/', UserListAPIView.as_view(), name='list_view'),
#     path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
#     path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
#     path('auth/', include('djoser.urls')),
#     re_path(r'^auth/', include('djoser.urls.authtoken')),
#
# ]
urlpatterns = [
    path('register/', UserViewSet.as_view({'post': 'create'}), name="register"),
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path("login/", TokenObtainPairView.as_view(), name="login"),
    path("resend-activation/", UserViewSet.as_view({"post": "resend_activation"}), name="resend_activation"),
    path("activation/<str:uid>/<str:token>/", UserViewSet.as_view({"post": "activate"}), name="activate"),
    path("reset-password/", UserViewSet.as_view({"post": "reset_password"}), name="reset_password"),
    path(
        "reset-password-confirm/<str:uid>/<str:token>/",
        UserViewSet.as_view({"post": "reset_password_confirm"}),
        name="reset_password_confirm"
    ),
]


# urlpatterns += router.urls
