from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    return render(request, "frontend/home.html")

def contactus(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()

    return render(request, "frontend/contactus.html")
