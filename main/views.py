from django.shortcuts import render

from main.models import *


# Create your views here.

def index(request):
    return render(request, 'index.html')


def news(request):
    posts = Post.objects.all()
    return render(request, 'news.html', {'active': 'news', 'posts': posts})


def single_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'singlePost.html', {'active': 'news', 'post': post})
