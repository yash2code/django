from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        'title' : 'Home page',
    }
    return render(request, "app/index.html",context)

def create(request):
    context={
        'title' : 'Create User',
    }
    return render(request, "app/create.html",context)
