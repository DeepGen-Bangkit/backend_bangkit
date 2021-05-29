from rest_framework import routers
from django.urls import path
from . import views
from rest_auth.views import (
    UserDetailsView
)
from rest_framework_jwt.views import refresh_jwt_token

router = routers.SimpleRouter()

urlpatterns = [
    path('users/login/', views.CustomLoginView.as_view(), name='account_login'),
    path('users/register/', views.CustomRegisterView.as_view(), name='account_signup'),
    path('users/profile/', UserDetailsView.as_view(), name="rest_user_details"),
    path('users/refresh-token/', refresh_jwt_token),
]
