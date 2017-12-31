from django.urls import include,path
from . import views
#from django.views.generic import TemplateView

app_name='app'

urlpatterns = [
    path('',views.index,name="home"),
    path('create',views.create,name="create"),
    #path('',TemplateView.as_view(template_name='app/index.html'),name="home")
]
