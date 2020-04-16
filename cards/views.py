from django.shortcuts import render
from .models import Cards
from logpage.models import Profile

def cards(request):
    cards = Cards.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)

        return render(request, 'cards/cards.html', {'tasks': cards, 'typeuser': typeuser})
    else:
        return render(request, 'cards/cards.html', {'tasks': cards})
