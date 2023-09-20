from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('dashboard', views.dashboard, name="Admin Dashboard"),
    path('view_client', views.view_client, name="view_client"),
    path('add_trainer', views.add_trainer, name="add_trainer"),
    path('trainers_requests', views.trainers_requests, name="trainers_requests"),
    path('add_programcategory', views.add_programcategory, name="add_programcategory"),
    path('add_training_program', views.add_training_program, name="add_training_program"),
    path('add_client', views.add_client, name="add_client"),
]