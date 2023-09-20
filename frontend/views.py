from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
# from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from panel.models import *
from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login
from django.utils import timezone


import re  # Import the regular expressions module
import bcrypt





class RegistrationView(View):
    def get(self, request):
        return render(request, 'frontend/register.html')

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password too short')
                    return render(request, 'frontend/register.html', context)

                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
                messages.success(request, 'Account successfully created')
                return render(request, 'frontend/register.html')

        return render(request, 'frontend/register.html')


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'sorry email in use,choose another one '}, status=409)
        return JsonResponse({'email_valid': True})


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'sorry username in use,choose another one '}, status=409)
        return JsonResponse({'username_valid': True})


# class LoginView(View):
#     def get(self, request):
#         return render(request, 'frontend/login.html')

#     def post(self, request):
#         username = request.POST['username']
#         password = request.POST['password']

#         if username and password:
#             user = auth.authenticate(username=username, password=password)

#             if user:
#                 if user.is_active:
#                     auth.login(request, user)
#                     messages.success(request, 'Welcome, ' +
#                                      user.username+' you are now logged in')
#                     return redirect('/')
#                 messages.error(
#                     request, 'Account is not active,please check your email')
#                 return render(request, 'frontend/login.html')
#             messages.error(
#                 request, 'Invalid credentials,try again')
#             return render(request, 'frontend/login.html')

#         messages.error(
#             request, 'Please fill all fields')
#         return render(request, 'frontend/login.html')


def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            # Retrieve the user from the Company model based on the provided email
            user = Company.objects.get(email=email)
            print(f"Email: {user.company_id}")
            print(f"Stored Password: {user.password}")
            # Verify the password
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                # Password is correct, log the user in
                request.session['user_id'] = user.company_id
                # messages.success(request, "Login successful")
                return redirect("home")  # Replace 'home' with the URL where you want to redirect after login
            else:
                # Password is incorrect, display an error message
                messages.error(request, "Invalid email or password")
                return redirect("login")  # Replace 'login' with the URL of your login page

        except Company.DoesNotExist:
            # User with the provided email doesn't exist, display an error message
            messages.error(request, "Invalid email or password")
            return redirect("login")  # Replace 'login' with the URL of your login page

    return render(request, 'frontend/login.html')



# class LogoutView(View):
#     def post(self, request):
#         auth.logout(request)
#         messages.success(request, 'You have been logged out')
#         return redirect('login')

def user_logout(request):
    # Clear session data
    request.session.clear()
    # Add a success message to inform the user about the successful logout
    messages.success(request, 'You have been logged out.')
    # Redirect to the login page
    return redirect('login')


def home(request):
    if 'user_id' not in request.session:
        # If the user is not logged in, redirect to the login page
        return redirect('login')

    user_id = request.session['user_id']
    user = Company.objects.get(pk=user_id)

    # Getting the data from panel models
    categories = ProgramCategory.objects.all()

    # Create a dictionary to store the first 4 training programs for each category
    training_programs_dict = {}
    for category in categories:
        programs = TrainingProgram.objects.filter(category=category)[:4]  # Limit to 4 programs per category
        training_programs_dict[category] = programs

    context = {
        'user': user,
        'categories': categories,
        'training_programs_dict': training_programs_dict,
    }
    return render(request, "frontend/home.html", context)

# pharmaceuticals
def pharmaceutical(request):
    if 'user_id' not in request.session:
        print("hello")
        # If the teacher is not logged in, redirect to the login page
        return redirect('login')

    user_id = request.session['user_id']
    user = Company.objects.get(pk=user_id)
    
    context={
        'user':user,
    }
    return render(request, "frontend/pharmaceuticals.html", context)

# cosmetics
def cosmetics(request):
    if 'user_id' not in request.session:
        print("hello")
        # If the teacher is not logged in, redirect to the login page
        return redirect('login')

    user_id = request.session['user_id']
    user = Company.objects.get(pk=user_id)
    
    context={
        'user':user,
    }
    return render(request, "frontend/cosmetics.html",context)


def whoweare(request):
    trainers = Trainer.objects.all()
    if 'user_id' not in request.session:
        print("hello")
        # If the teacher is not logged in, redirect to the login page
        return redirect('login')

    user_id = request.session['user_id']
    user = Company.objects.get(pk=user_id)
    
    context={
        'user':user,
        'trainers': trainers
    }
    return render(request, "frontend/whoweare.html", context)


def trainers(request):
    if 'user_id' not in request.session:
        print("hello")
        # If the teacher is not logged in, redirect to the login page
        return redirect('login')

    user_id = request.session['user_id']
    user = Company.objects.get(pk=user_id)
    
    trainers = Trainer.objects.all()
    context={
        'user':user,
        'trainers': trainers
    }
    
    return render(request, "frontend/trainers.html", context)

# single Trainer
def trainer_details(request, id):
    if 'user_id' not in request.session:
        print("hello")
        # If the teacher is not logged in, redirect to the login page
        return redirect('login')

    user_id = request.session['user_id']
    user = Company.objects.get(pk=user_id)

    trainer = get_object_or_404(Trainer, pk=id)
    
    context={
        'user':user,
        'trainer': trainer
    }
    
    return render(request, 'frontend/trainer_details.html', context)

# create account view

def create_account(request):
    if request.method == "POST":
        company_name = request.POST.get("company_name")
        company_location = request.POST.get("company_location")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        company_type = request.POST.get("company_type")
        profile_image = request.FILES.get('profile_image')
        password = request.POST.get("password")  # Get the password from the form
        confirm_password = request.POST.get("confirm_password")  # Get the confirmation password

        this_user = Company.objects.get(email=email)

        if(this_user):
            messages.error(request, "User with this email already exists, try again")
            return redirect("/create_account")
        
        else:
            # Check if the password meets the criteria
            if (
                len(password) < 8 or  # Check if the password is at least 8 characters long
                not re.search(r'[A-Z]', password) or  # Check if there's at least one uppercase letter
                not re.search(r'[!@#$%^&*]', password)  # Check if there's at least one symbol
            ):
                messages.error(request, "Password should contain a symbol and uppercase letter with atleast 8 characters")
                return redirect("/create_account")

            if password != confirm_password:
                messages.error(request, "Passwords do not match, please try again")
                return redirect("/create_account")

            # Encrypt the password using bcrypt
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            client = Company.objects.create(
                company_name=company_name,
                company_location=company_location,
                phone_number=phone_number,
                email=email,
                company_type=company_type,
                password=hashed_password.decode('utf-8'),  # Store the hashed password
            )

            if profile_image:
                fs = FileSystemStorage()
                image_filename = fs.save(profile_image.name, profile_image)
                client.profile_image = image_filename

            client.save()
            messages.success(request, "Client registered successfully")
            return redirect("/create_account")
    else:
        return render(request, "frontend/user_registration.html")


def trainings(request):
    if 'user_id' not in request.session:
        # If the teacher is not logged in, redirect to the login page
        return redirect('login')

    user_id = request.session['user_id']
    user = Company.objects.get(pk=user_id)
    
    context={
        'user':user,
    }
    return render(request, 'frontend/trainings.html',context)

# training views
def program_details(request, program_id):
    if 'user_id' not in request.session:
        # If the teacher is not logged in, redirect to the login page
        return redirect('login')

    user_id = request.session['user_id']
    user = Company.objects.get(pk=user_id)

    this_program = TrainingProgram.objects.get(pk=program_id)
    
    context={
        'user':user,
        'this_program':this_program
    }
    
    return render(request, 'frontend/program_details.html',context)

def request_program(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        program_id = request.POST.get("program_id")


        user = Company.objects.get(pk=user_id)
        program = TrainingProgram.objects.get(pk=program_id)

        existing_request = Request.objects.filter(user_id=user, training_program=program).first()
        if existing_request:
            messages.error(request, "You already enrolled fro this Training program")
            return redirect("program_details", program_id=program_id)

        date = timezone.now()

        program_request = Request.objects.create(
            training_program=program,
            user_id=user,
            date_of_training = date
        )

        program_request.save()
        messages.success(request, "Enrollment successfull")

        return redirect("program_details", program_id=program_id)

def validation(request):
    return render(request, 'frontend/trainings/instrument_validation.html')
def calibration(request):
    return render(request, 'frontend/trainings/instrument_calibration.html')
def operation(request):
    return render(request, 'frontend/trainings/instrument_operation.html')
def data_analysis(request):
    return render(request, 'frontend/trainings/instrument_data_analysis.html')