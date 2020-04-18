from django.urls import path

from . import views

urlpatterns = [
    path('', views.playgrounds, name='playgrounds'),
    path('newplay/', views.newplay, name='newplay'),
    path('myplays/', views.myplays, name='myplays'),
]
