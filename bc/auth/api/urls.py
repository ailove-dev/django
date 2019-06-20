from django.urls import path

from . import views

app_name = "auth"

urlpatterns = [
    path("login", views.LoginAPIView.as_view(), name="login"),
    path("logout", views.LogoutAPIView.as_view(), name="logout"),
]
