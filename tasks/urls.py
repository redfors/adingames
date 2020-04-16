from django.urls import re_path

from . import views

urlpatterns = [
    re_path('', views.mytasks, name='tasks'),
    re_path('feed/', views.feed, name='feed')
]