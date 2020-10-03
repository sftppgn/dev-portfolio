from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import random
from .models import Blog 

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/home.html', {'blogs':blogs}) 
#def all_blogs(request):
#    return render(request, 'blog/all_blogs.html', {'blogs':blogs})
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'id': blog})