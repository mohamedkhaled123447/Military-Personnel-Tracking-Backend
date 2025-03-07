from django.urls import path
from .views import CreateUserView, LoginView, ActivationView,ResetPassword
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views import CustomTokenObtainPairView

urlpatterns = [
    path("create-user/", CreateUserView.as_view(), name="create-user"),
    path("login/", LoginView.as_view(), name="login"),
    path("activate/", ActivationView.as_view(), name="activate"),
    path("reset-password/", ResetPassword.as_view(), name="reset_password"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
