from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "frontend/home.html")

# pharmaceuticals
def pharmaceutical(request):
    return render(request, "frontend/pharmaceuticals.html")

# cosmetics
def cosmetics(request):
    return render(request, "frontend/cosmetics.html")