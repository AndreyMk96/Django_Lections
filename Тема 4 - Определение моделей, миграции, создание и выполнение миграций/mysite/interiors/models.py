from django.db import models


class Interior(models.Model):  # Класс наследуется от базового класса models.Model
    # Поле id не прописывается. Оно есть в базовом классе
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)  # Может быть пустым
    photo = models.ImageField(upload_to="photos/%Y/%m%d/")  # Указываются каталоги и подкаталоги загрузки
    time_create = models.DateTimeField(auto_now_add=True)  # Принимает текущее время в момент добавления новой записи
    time_update = models.DateTimeField(auto_now=True)  # Принимает текущее время при изменении записи
    is_published = models.BooleanField(default=True)  # По умолчанию значение True
