# Фреймворк Django использует модель MTV
# Модель MTV (models, templates, views)
# В этой модели по запросам от пользователя ищется шаблон на сайте
# Если шаблон не найден выдается ошибка 404

# В settings.py в разделе INSTALLED APPS необходимо прописать название инсталлируемого приложения
# В нашем случае interior.apps.InteriorConfig

# Создадим обработчик главной страницы сайта в interiors -> views(функция index)
# Далее добавляем маршрут в urls.py (path('interios/', index))

# Создание заголовка в функции categories
# В список маршрутов также добавляется этот маршрут

# После добавления маршрутов, страница без указания маршртов перестает работать.
# Чтобы она снова начала работать, в списке маршрутов надо пропистаь пустую строчку

# Однако все ссылки проще сделать в отдельном файле urls
# Особенно это поможет при копировании иили переносе сайта

# path('interiors/', include("interiors.urls"))
# Подключение оновного окна через urls, для создния иерархии страниц