from django.contrib import admin
from django.urls import path, include 
from weather_app.views import weather_info 

urlpatterns = [
    path('', weather_info, name='weather_info'),
]
