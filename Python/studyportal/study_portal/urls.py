from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("course", views.course1, name="course"),


]
