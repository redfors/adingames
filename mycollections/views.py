from django.shortcuts import render
from .models import Mycollections
from logpage.models import Profile


def mycollections(request):
    collections = Mycollections.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'mycollections/collections.html', {'collections': collections, 'typeuser': typeuser})
    else:
        return render(request, 'mycollections/collections.html', {'collections': collections})


def newcollection(request):
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)

        return render(request, 'mycollections/new.html', {'typeuser': typeuser})
    else:
        return render(request, 'mycollections/new.html')
