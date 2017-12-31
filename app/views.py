from django.shortcuts import render
from app.forms import ProfileForm
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    context={
        'title' : 'Home page',
    }
    return render(request, "app/index.html",context)


def add(request):
    form_class = ProfileForm
    form = form_class(request.POST or None)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
    # create a form instance and populate it with data from the request:
        form = ProfileForm(request.POST)
    # check whether it's valid:
        if form.is_valid():
    # Save a new Profile object from the form's data.
            new_profile = form.save()

            return render(request, 'app/index.html', {'form':form})
            

    return render(request, 'app/create.html', {'form': form}) 

''' class CreateView(TemplateView):
    template_name = 'app/create.html'

    def get(self,request):
        form = ProfileForm()
        return render(request, self.template_name, {'form':form}) '''


    

