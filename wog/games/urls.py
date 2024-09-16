"""
URL configuration for games app
"""

from django.urls import URLPattern, path
from . import views

urlpatterns: list[URLPattern] = [
    path("guessing-game", views.guessing_game, name="guessing_game")
]
