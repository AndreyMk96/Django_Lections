"""Тема 5 - CRUD основы работы с моделями"""

"""CRUD - Create, Read, Update, Delete"""

# Каждый экземпляр класса Interior, представляет строго одну запись БД Interiors(одну строку)

# Для перехода в консоль django
"""python manage.py shell"""

# Импорт модели
# from interiors.models import Interior

# Добавляем запись в таблицу через создание экземпляра класса
# Interior(title = "Спальня", content = "Спальное место принцессы")

# в i1 сохраняем последний созданный объект(иначе запись не добавится)

# i1 = _i1
# i1.save()

# Просмотреть данные объекта:
# i1.id, i1.title и т д.

# i1.pk - номер записи(идентификатор в django)

# Добавим еще одну запись
"""i2 = Interior(title = "Спальня улучшенная", content = "Спальное место принцессы улучшенное")
>>> i2.save()
"""

# История sql запросов
""">>> from django.db import connection
>>> connection.queries
"""

# Каждый класс модели содержит статический объект objects. Через него можно делать различные полезные действия
""">>> i4 = Interior.objects.create(title = "Спальня детская современная", content = "Спальня детская современная лофт")
вызывать можно без присвоения к объекту 
Interior.objects.create(title = "Спальня детская современная", content = "Спальня детская современная лофт")
"""

# Считать все объекты записей
""">>> Interior.objects.all()
чтобы заработало необходимо перезапустить проект"""

# Вывод отдельного элемента
""">>> lst = Interior.objects.all()
>>> lst[0]
"""

# Перебор циклом
""">>> for el in lst:
...     print(el.content)
"""

# Фильтрация
""">>> Interior.objects.filter(title = "Спальня")"""

# Сравнение
"""<Имя атрибута>__gte - сравнение больше или равно (>=)
<Имя атрибута>__lte - сравнение меньше или равно (<=)"""

# Запрос со сравнением
""">>> Interior.objects.filter(pk__gte=2)
>>> Interior.objects.filter(pk__lte=3)"""

# Выборка записей, не соответствующих условию
""">>> Interior.objects.exclude(pk=3)"""

# Получать конкретную запись лучше через метод get
"""Interior.objects.get(pk=1)"""
"""Метод get генерирует исключение, если возвращается более одной записи или не возвращается ни одной записи
Это нужно например при авторизации"""

# Сортировка записей
""">>> Interior.objects.order_by("title")"""

# Обратная сортирока через знак минус
""">>> Interior.objects.order_by("-title")"""

# Изменение записи
"""
>>> new_i2 = Interior.objects.get(pk=2)
>>> new_i2.title = "Спальня улучшенная новая"
>>> new_i2.save()
"""

# Удаление объекта
""">>> del_obj = Interior.objects.get(pk=4)
>>> del_obj.delete()"""
