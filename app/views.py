from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        'title' : 'Home page',
    }
    return render(request, "app/index.html",context)
