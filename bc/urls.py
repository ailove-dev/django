from django.urls import include, path

app_name = "bc"

urlpatterns = [
    path("auth/", include("bc.auth.api.urls")),
    path("courses/", include("bc.courses.api.urls")),
    path("users/", include("bc.users.api.urls")),
    path("common/", include("bc.common.api.urls")),
]
