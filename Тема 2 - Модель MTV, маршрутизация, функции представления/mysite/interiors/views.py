from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):  # HTTP Request
    return HttpResponse("Страница приложения интерьеры")


def categories(request):
    return HttpResponse("<H1>Статьи по категориям<H1>")
