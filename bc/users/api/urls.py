from django.urls import path

from . import views

app_name = "users"

urlpatterns = [path("current", views.UserRetrieveAPIView.as_view(), name="current")]
