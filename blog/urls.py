from django.urls import re_path

from . import views

urlpatterns = [
    re_path('', views.blog, name='blog'),
]