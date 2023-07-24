from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('pharmaceutical/', views.pharmaceutical),
    path('cosmetics/', views.cosmetics),
]