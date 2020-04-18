from django.shortcuts import render
from .models import Deals, DealManager
from logpage.models import Profile

def deals(request):
    deals = Deals.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'deals/deals.html', {'deals': deals, 'typeuser': typeuser})
    else:
        return render(request, 'deals/deals.html', {'deals': deals})

def dealmanager(request):
    dealmanager = DealManager.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'deals/dealmanager.html', {'dealmanager': dealmanager, 'typeuser': typeuser})
    else:
        return render(request, 'deals/dealmanager.html', {'dealmanager': dealmanager})
