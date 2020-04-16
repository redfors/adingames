from django.shortcuts import render
from .models import Deals
from logpage.models import Profile

def deals(request):
    deals = Deals.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'deals/deals.html', {'deals': deals, 'typeuser': typeuser})
    else:
        return render(request, 'deals/deals.html', {'deals': deals})
