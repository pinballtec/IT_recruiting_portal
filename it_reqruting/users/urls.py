from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('registration/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
