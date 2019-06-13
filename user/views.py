from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'user/index.html')


def register(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'user/register.html', {'form': form})
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponse("<p> register post</p>")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if(user is not None):
            login(request, user)
            messages.success(request, 'Welcome to Project Hunt')
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect(request.META['HTTP_REFERER'])


def dashboard(request):
    pass
