from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'user/index.html')


def register(request):
    # form = UserCreationForm()
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == "POST":
        print(request.POST)
        return  HttpResponse("<p> register post</p>")
