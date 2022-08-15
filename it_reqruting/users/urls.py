from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('registration/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profiles/', views.profiles, name='profiles'),
    path('profile/<str:username>/', views.userProfile, name="user-profile"),
    path('inbox/', views.indox, name="inbox"),
]
