from django.urls import re_path
from django.views.generic import TemplateView

app_name = "skels_manager"
urlpatterns = [
    re_path(r"", TemplateView.as_view(template_name="base.html")),
]
