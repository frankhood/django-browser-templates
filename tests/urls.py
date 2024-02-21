from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    path("skels/", include("skels_manager.urls", namespace="skels_manager")),
]
