from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path("", views.CourseListAPIView.as_view(), name="list"),
    path(
        "current/<int:module_id>",
        views.CourseModuleRetieveAPIView.as_view(),
        name="module",
    ),
]
