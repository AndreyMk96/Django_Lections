# Моделаь отвечает за хранение и оперирование данными с сайта
# ORM(Object relational mapping, объектно - реляционное отображение) - Механизм взаимодействия с БД(встроенный в django)
# Модель ORM может взаимодействовать с любым типом БД

# settings.py/databases - настройки БД
# База хранится в каталоге проекта

# Чтобы создать таблицу в БД, достаточно создать ее модель и выполнить миграцию.
# Модели создаются в interiors/models
# Класс модели наследуется от базового клас


# В settings.py добавляем
"""# Добавим описание двух констант
MEDIA_ROOT = os.path.join(BASE_DIR, "media")  # Путь к каталогу media. BASE_DIR - это директория с проектом
MEDIA_URL = '/media/'  # Добавление префикса media к URL графических файлов"""

# Класс Interior в Models.py

"""class Interior(models.Model):  # Класс наследуется от базового класса models.Model
    # Поле id не прописывается. Оно есть в базовом классе
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)  # Может быть пустым
    photo = models.ImageField(upload_to="photos/%Y/%m%d/")  # Указываются каталоги и подкаталоги загрузки
    time_create = models.DateTimeField(auto_now_add=True)  # Принимает текущее время в момент добавления новой записи
    time_update = models.DateTimeField(auto_now=True)  # Принимает текущее время при изменении записи
    is_published = models.BooleanField(default=True)  # По умолчанию значение True"""

# В режиме отладки к маршрутам добавляем еще один маршрут к статическим данным в urls
"""if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)"""
# Чтобы корректно работало DEBUG меняем на True

# миграции - это модули языка Python где описаны наборы команд на уровне ОРМ интерфейса.
# файл миграций помещается в папку migrations

# Вывести sql - запрос миграцииpython
"""python manage.py sqlmigrate interiors 0001"""

# Выполнить миграцию
"""python manage.py migrate"""
# Помимо созданной модели имеются вспомогательные модели по умолчанию
# Теперь можно проверить в sqlite studio создалась ли БД
