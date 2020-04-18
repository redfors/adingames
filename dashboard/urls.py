from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashaboard, name='index'),
]