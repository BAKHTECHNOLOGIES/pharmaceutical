from django.urls import path
from . import views
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('home', views.home, name="home"),

    path('pharmaceutical/', views.pharmaceutical),
    path('cosmetics/', views.cosmetics),
    path('trainers', views.trainers),
    path('trainings/', views.trainings, name="training programs"),
    path('trainers/<int:id>/', views.trainer_details, name='trainer_details'),
    path('whoweare', views.whoweare, name='whoweare'),
    path('register', RegistrationView.as_view(), name="register"),
    # path('login', LoginView.as_view(), name="login"),

    path('', views.user_login, name="login"),
    path('logout', views.user_logout, name="logout"),
    # path('logout', LogoutView.as_view(), name="logout"),

    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),name='validate_email'),

    path('create_account/', views.create_account,name='create_account'),


    # training urls
    path('instrument_validation/', views.validation, name="Instrument validation"),
    path('instrument_operation/', views.operation, name="Instrument operation   "),
    path('instrument_calibration/', views.calibration, name="Instrument calibration"),
    path('instrument_validation/', views.validation, name="Instrument validation"),
    path('instrument_calibration/', views.calibration, name="Instrument calibration"),
    path('instrument_operation/', views.operation, name="Instrument operation   "),
    path('instrument_data_analusis/', views.data_analysis, name="Instrument data analysis   "),

    path('program_details/<program_id>', views.program_details, name="program_details"),
    path('request_program/', views.request_program, name="request_program"),

         

]