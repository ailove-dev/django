from django.urls import path

from . import views

app_name = "common"

urlpatterns = [path("areas", views.AreaListAPIView.as_view(), name="list")]
