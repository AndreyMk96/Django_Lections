from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# Create your views here.


def index(request):  # HTTP Request
    return HttpResponse("Страница приложения интерьеры")


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
