from django.shortcuts import render

from main.models import *


# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})
