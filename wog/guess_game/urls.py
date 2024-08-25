"""
URL configuration for Guess Game app
"""

from django.urls import URLPattern, path
from . import views

urlpatterns: list[URLPattern] = [
    path("", views.test_render)
]
