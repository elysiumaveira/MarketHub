from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserDetailView, UserRegisterView, UserLogOutView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='log_in'),
    path('log_out/', UserLogOutView.as_view(), name='log_out'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user_detail/', UserDetailView.as_view(), name='user_detail'),
]
