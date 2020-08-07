from django.shortcuts import render

from main.models import *


# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html')


def news(request):
    posts = Post.objects.all()
    return render(request, 'news.html', {'posts': posts})
