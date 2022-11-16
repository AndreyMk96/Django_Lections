"""Тема 6 - Шаблоны"""

# Обновим функцию index
"""def index(request):  # HTTP Request
    #return HttpResponse("Страница приложения интерьеры")
    return render(request, 'interiors/index.html')  # Второй параметр - путь к шаблону, templates в пути указывать не нужно"""

# Далее создадим в interiors папку templates, где будут храниться шаблоны
# А в этом каталоге создается подкаталог с именем нашего приложения
# В этом подкаталоге создаем файл index.html

"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title> Главная страница</title>
</head>
<body>

</body>
</html>"""

# Создадим еще один файл about.html он будет содержать информацию о сайте
"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>О сайте</title>
</head>
<body>
    <h1>О сайте</h1>
</body>
</html>"""

# Добавим функцию about во views
"""def about(request):
    return render(request, 'interiors/about.html')
"""

# Добавим в urlpatterns
"""path('about/', about, name="about")"""

# В index.html в заголовке добавим переменную titles
"""<title>{{title}}</title>"""
# Тоже самое в about.html
# Переменные передаются во views третьим параметром
"""def about(request):
    return render(request, 'interiors/about.html', {"title":"О сайте"})"""

# Добавим во views список для главного меню
menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

# И добавим его в передаваемые параметры
"""def index(request):  # HTTP Request
    #return HttpResponse("Страница приложения интерьеры")
    return render(request, 'interiors/index.html', {"menu": menu, "title": "Главная страница"})  # Второй параметр - путь к шаблону, templates в пути указывать не нужно
"""

# Отразим элементы меню в теле главной страницы
"""<body>
<ul>
    {% for m in menu %}
    <li>{{m}}</li>
    {% endfor %}
</ul>
</body>"""

# Тоже самое добавим в about

# Если присмотреться index.html и about.html имеют одно и тоже содержимое, тем самым нарушается принцип DRY
# Для этого обычно создается базовый шаблон, добавим base.html
"""<!DOCTYPE html>
<html>
<head>
    <title>{{title}}</title>
</head>
<body>
{% block mainmenu %}
<ul>
  {% for m in menu %}
  <li> {{m}} </li>
  {% endfor %}
</ul>
{% endblock mainmenu %}
{% block content %}
{% endblock %}
</body>
</html>"""

# Считаем данные из базы
# Импортируем models во views.py
"""from .models import *"""

# Передадим данные в функцию index
"""def index(request):  # HTTP Request
    #return HttpResponse("Страница приложения интерьеры")
    posts = Interior.objects.all()
    return render(request, 'interiors/index.html', {"posts": posts, "menu": menu, "title": "Главная страница"})  # Второй параметр - путь к шаблону, templates в пути указывать не нужно
"""

# И поправим index.html
"""{% extends "interiors/base.html" %}

{% block content %}
<h1> {{title}} </h1>
<ul>
    {% for p in posts %}
    <li>
        <h2>{{p.title}}</h2>
        <p>{{p.content}}</p>
        <hr>
    </li>
    {% endfor %}
</ul>
{% endblock %}
"""