from weather.views import WeatherView
from . import views
from django.urls import path

urlpatterns = [
    path('', WeatherView.as_view(), name="weather-main")
]
