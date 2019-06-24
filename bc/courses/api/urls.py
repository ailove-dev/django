from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path("", views.CourseViewSet.as_view({"get": "list"}), name="list"),
    path("current/", views.CourseViewSet.as_view({"get": "retrieve"}), name="current"),
    path(
        "current/<int:module_id>",
        views.CourseModuleRetieveAPIView.as_view(),
        name="module",
    ),
]
