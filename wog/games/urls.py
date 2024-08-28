"""
URL configuration for Games app
"""

from django.urls import URLPattern, path
from . import views

urlpatterns: list[URLPattern] = [
    path("", views.test_render)
]
