from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'panel/dashboard.html')


def add_company(request):
    if request.method == "GET":
        return render(request, 'panel/company.html')
    else:
        # add_company code 
        return render(request, 'panel/company.html')


def add_programcategory(request):
    if request.method == "GET":
        return render(request, 'panel/program_category.html')
    else:
        # add_programcategory Code
        return render(request, 'panel/program_category.html')
    

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