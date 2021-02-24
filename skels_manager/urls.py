from django.conf.urls import url

from .views import SkelView 

urlpatterns = (
    url(r'^(?P<template_name>.*?)/?$', SkelView.as_view(), name="skels-preview"),
)