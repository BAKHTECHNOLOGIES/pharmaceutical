from django.urls import path
from . import views
from .views import RegistrationView,LogoutView,LoginView,UsernameValidationView,EmailValidationView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home),
    path('trainers', views.trainers),
    path('trainers/<int:id>/', views.trainer_details, name='trainer_details'),
    path('whoweare', views.whoweare, name='whoweare'),
    path('register', RegistrationView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),name='validate_email')
         
]