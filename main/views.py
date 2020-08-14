from django.shortcuts import render, redirect
from django.contrib import auth

from main.models import *


# Create your views here.

def index(request):
    author = ''
    if request.user.is_authenticated:
        author = ExtendedUser.objects.get(user=request.user)
    return render(request, 'index.html', {'author': author})


def news(request):
    posts = Post.objects.all()
    return render(request, 'news.html', {'active': 'news', 'posts': posts})


def single_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'singlePost.html', {'active': 'news', 'post': post})


def login(request):
    form_info = [
        {
            'input': 'login',
            'label': 'Логин',
            'type': 'text',
            'required': True,
        },
        {
            'input': 'password',
            'label': 'Пароль',
            'type': 'password',
            'required': True,
        }]
    if request.POST:
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            next_to = request.GET.get('next', '/')
            return redirect(next_to)
        else:
            form_info[0]['value'] = username
            form_info[1]['error'] = 'Неверный логин или пароль'

    return render(request, 'login.html', {'form_info': form_info})


def register(request):
    form_info = [
        {
            'input': 'first_name',
            'label': 'Имя',
            'type': 'text',
            'required': True,
        },
        {
            'input': 'last_name',
            'label': 'Фамилия',
            'type': 'text',
            'required': True,
        },
        {
            'input': 'username',
            'label': 'Ник',
            'type': 'text',
            'required': True,
        },
        {
            'input': 'email',
            'label': 'Email',
            'type': 'email',
            'required': True,
        },
        {
            'input': 'social',
            'label': 'Ссылка на социальную сеть для связи',
            'type': 'url',
            'required': True,
        },
        {
            'input': 'password',
            'label': 'Пароль',
            'type': 'password',
            'required': True,
        },
        {
            'input': 'password-repeat',
            'label': 'Повторите пароль',
            'type': 'password',
            'required': True,
        },

    ]
    if request.POST:
        # TODO сделать лучше
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        social = request.POST.get('social')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password-repeat')
        form_info[0]['value'] = first_name
        form_info[1]['value'] = last_name
        form_info[2]['value'] = username
        form_info[3]['value'] = email
        form_info[4]['value'] = social
        form_info[5]['value'] = password
        form_info[6]['value'] = password_repeat
        user_exist = User.objects.filter(username=username)
        if user_exist.count() != 0:
            form_info[2]['error'] = 'Такой пользователь уже существует'
        elif password != password_repeat:
            form_info[6]['error'] = 'Пароли не совпадают'
        else:
            user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name,
                                            password=password)
            user.save()
            ext_user = ExtendedUser.objects.create(user=user, socialLink=social)
            ext_user.save()
            auth.login(request, user)
            return redirect('/')

    return render(request, 'register.html', {'form_info': form_info})
