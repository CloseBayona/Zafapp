from django.contrib import admin
from django.urls import path, include

from main import views


urlpatterns = [
    path('', views.home, name='Home'),
    path('history', views.makeHistory, name='History'),
    path('filter', views.histFilter, name='Filter')
]