from django.shortcuts import render
from .models import Mytools


def mytools(request):
    mytools = Mytools.objects.all()
    return render(request, 'mytools/mytools.html', {'mytools': mytools})
