# from django.contrib import admin
from django.urls import path ,include
from .import views
urlpatterns = [
    path("", views.Input, name="Input"),
    path("Data", views.Store, name="Store"),
]