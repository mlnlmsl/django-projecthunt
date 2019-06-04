from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'user/index.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == "POST":
        pass
