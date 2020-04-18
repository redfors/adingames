from django.urls import path

from . import views

urlpatterns = [
    path('', views.mycollections, name='collections'),
    path('new', views.newcollection, name='new')
]