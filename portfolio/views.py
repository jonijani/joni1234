from django.shortcuts import render
from .models import Project

def home(request):
    joni = Project.objects.all()
    return render(request , 'portfolio/home.html', {'zak': joni})

# Create your views here.
