from django.shortcuts import render
from .models import Deals


def deals(request):
    deals = Deals.objects.all()
    return render(request, 'deals/deals.html', {'deals': deals})
