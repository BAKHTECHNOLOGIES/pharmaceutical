from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request, 'panel/dashboard.html')


def view_client(request):
    if request.method == "GET":
        return render(request, 'panel/company.html')
    else:
        # add_company code 
        return render(request, 'panel/company.html')

def add_client(request):
    if request.method == "GET":
        return render(request, 'panel/addclient.html')
    else:
        # add_company code 
        return render(request, 'panel/addclient.html')

# view for adding a category
def add_programcategory(request):
    if request.method == "POST":
        category_name = request.POST.get("category_name")
        this_category = ProgramCategory.objects.filter(category_name=category_name)

        if this_category:
            messages.error(request,"Category already exists")
            return redirect("add_programcategory")
        
        else:
            program_category = ProgramCategory.objects.create(category_name=category_name)
            program_category.save
            messages.success(request, "Category has successfully been added")
            return redirect("add_programcategory")
    else:
        # add_programcategory Code
        context={
            "categories": ProgramCategory.objects.all()
        }
        return render(request, 'panel/program_category.html', context)

#view for deleting a category
def delete_category(request):
    if request.method == "POST":
        cat_id = request.POST.get("cat_id") 
        this_category = ProgramCategory.objects.filter(category_id=cat_id)

        this_category.delete()
        messages.success(request,"Category deleted successfully")
        return redirect("add_programcategory")

#view for editing category name
def edit_category(request):
    if request.method == "POST":
        cat_id = request.POST.get("cat_id")
        category_name = request.POST.get("category_name")

        this_category = ProgramCategory.objects.get(category_id=cat_id)
        this_category.category_name = category_name
        this_category.save()
        messages.success(request,"Category edited successfully")
        return redirect("add_programcategory")


def add_training_program(request):
    if request.method == "GET":
        return render(request, 'panel/training_program.html')
    else:
        # training_program Code
        return render(request, 'panel/training_program.html')
    

def add_trainer(request):
    if request.method == "GET":
        return render(request, 'panel/trainers.html')
    else:
        # trainers Code
        return render(request, 'panel/trainers.html')
    

def trainers_requests(request):
    if request.method == "GET":
        return render(request, 'panel/trainers_requests.html')
    else:
        # trainers Code
        return render(request, 'panel/trainers_requests.html')