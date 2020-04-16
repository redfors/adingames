from django.shortcuts import render
from .models import Dealmanager
from logpage.models import Profile

def dealmanager(request):
    dealmanager = Dealmanager.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'dealmanager/dealmanager.html', {'dealmanager': dealmanager, 'typeuser': typeuser})
    else:
        return render(request, 'dealmanager/dealmanager.html', {'dealmanager': dealmanager})
