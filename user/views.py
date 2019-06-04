from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'user/index.html')


def register(request):
    form = UserCreationForm()
    if request.method == 'GET':
        return render(request, 'user/register.html',{'form':form})
    elif request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        passowrd = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if passowrd != confirm_password:
            messages.error(request, 'Password must match')

        return HttpResponse("<p> register post</p>")
