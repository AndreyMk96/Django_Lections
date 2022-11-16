from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

# Create your views here.

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):  # HTTP Request
    #return HttpResponse("Страница приложения интерьеры")
    posts = Interior.objects.all()
    return render(request, 'interiors/index.html', {"posts": posts, "menu": menu, "title": "Главная страница"})  # Второй параметр - путь к шаблону, templates в пути указывать не нужно


def about(request):
    return render(request, 'interiors/about.html', {"menu": menu, "title":"О сайте"})

def categories(request, category_id):
    if request.GET:  # Если GET - Запрос не пустой
        print(request.GET)
    return HttpResponse(f"<H1>Статьи по категориям</H1><p>Категория номер {category_id}</p>")


def archive(request, year):
    if int(year) > 2022:  # Если год более 2022
        # raise Http404
        return redirect("home", permanent=True)  # Редирект на главную страницу
    return HttpResponse(f"<H1>Каталог интерьеров за {year} год</H1>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<H1>Страница не найдена</H1>")



