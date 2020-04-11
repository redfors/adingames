"""adingames URL Configuration

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
from django.contrib import admin
from django.urls import include, re_path

from django.conf import settings

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'^$', include('advertiser.urls')),
    re_path(r'index/$', include('advertiser.urls')),
    re_path(r'blog/$', include('blog.urls')),
    re_path(r'cards/$', include('cards.urls')),
    re_path(r'chat/$', include('chat.urls')),
    re_path(r'contractors/$', include('contractors.urls')),
    re_path(r'dealmanager/$', include('dealmanager.urls')),
    re_path(r'deals/$', include('deals.urls')),
    re_path(r'login/$', include('logpage.urls')),
    re_path(r'mycollections/$', include('mycollections.urls')),
    re_path(r'mymessages/$', include('mymessages.urls')),
    re_path(r'myprofile/$', include('myprofile.urls')),
    re_path(r'mytools/$', include('mytools.urls')),
    re_path(r'newcard/$', include('newcard.urls')),
    re_path(r'newplaygrounds/$', include('newplayground.urls')),
    re_path(r'newspage/$', include('newspage.urls')),
    re_path(r'newtask/$', include('newtask.urls')),
    re_path(r'playgrounds/$', include('playgrounds.urls')),
    re_path(r'statistic/$', include('statistic.urls')),
    re_path(r'tasks/$', include('tasks.urls')),

]
