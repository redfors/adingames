from django.urls import path

from . import views

urlpatterns = [
    path('', views.deals, name='deals'),
    path('dealmanager/', views.dealmanager, name='dealmanager'),
]
