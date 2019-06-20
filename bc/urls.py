from django.urls import include, path

app_name = "bc"

urlpatterns = [path("auth/", include("bc.auth.api.urls"))]
