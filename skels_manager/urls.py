from django.urls import re_path

from .views import SkelView

app_name = "skels_manager"

urlpatterns = [
    re_path(r"^(?P<template_name>.*?)/?$", SkelView.as_view(), name="skels-preview"),
]
