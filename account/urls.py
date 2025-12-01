from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # path("register/", CreateUserView.as_view(), name="register_user"),
    path(
        "token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # noqa E501
    path(
        "token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # noqa E501
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
