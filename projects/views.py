from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'projects/home.html', {'projects':projects}) 
