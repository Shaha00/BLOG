from django.shortcuts import HttpResponse, redirect
from datetime import datetime


# Create your views here.


def main(request):
    return HttpResponse('Its my first view')


def google(request):
    return redirect('https://google.com')


def youtube(request):
    return redirect('https://youtube.com')


def github(request):
    return redirect('https://github.com')


def hello(request):
    return HttpResponse("Привет! Это мой первый проект")


def date(request):
    return HttpResponse(f"Дата: {datetime.now().date()}")


def goodbye(request):
    return HttpResponse("До встречи, Пользователь!")
