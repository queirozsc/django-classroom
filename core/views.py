from django.shortcuts import render
from django.views.generic import TemplateView

def home(request):
    return render(request, 'site/home.html')
# class Home(TemplateView):
#     template_name = 'home.html'