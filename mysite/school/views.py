from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .models import Blog, Day_Sub_Class


def sign_up(request):
    form = UserCreationForm
    return render(request, 'registration/sign_up.html', context={"form": form})


def view_list(request):
    items = Blog.objects.all()
    return render(request, 'list.html', context={'items': items})


def view_list_class(request, ):
    user = User
    classes = Day_Sub_Class.objects.all()
    return render(request, 'list_class.html', context={'classes': classes,
                                                       'user': user})
