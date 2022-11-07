from django.urls import path, re_path
from .views import *



urlpatterns = [
    path("", index, name="home"), # http://127.0.0.1:8000/interiors
    path("categories/<category_id>/", categories),  # http://127.0.0.1:8000/interiors/categories
    re_path(r"archive/(?P<year>[0-9]{4})/", archive)
]