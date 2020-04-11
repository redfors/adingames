from django.shortcuts import render
from .models import Dealmanager


def dealmanager(request):
    dealmanager = Dealmanager.objects.all()
    return render(request, 'dealmanager/dealmanager.html', {'dealmanager': dealmanager})
