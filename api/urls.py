from django.urls import path
from . import views

# Mapping all url to it controllers

urlpatterns = [
    path('', views.index, name='index')
]