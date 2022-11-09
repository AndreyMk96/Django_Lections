"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from interiors.views import *
from mysite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('interiors/', index),  # http://127.0.0.1:8000/interiors
    # path("categories/", categories),  # http://127.0.0.1:8000/categories
    # path('', index),  # http://127.0.0.1:8000/interiors страница по умолчанию
    path('', include("interiors.urls"))

]

handler404 = page_not_found

# В режиме отладки к маршрутам добавляем еще один маршрут к статическим данным
# На реальных серверах этот процесс обычно настроен
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)