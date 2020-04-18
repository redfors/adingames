from django.urls import path

from tasks import views

urlpatterns = [
    path('', views.mytasks, name='tasks'),
    path('feed/', views.feed, name='feed'),
    path('newtask/', views.newtask, name='newtask'),
]
