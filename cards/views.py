from django.shortcuts import render
from .models import Cards


def cards(request):
    cards = Cards.objects.all()
    return render(request, 'cards/cards.html', {'tasks': cards})
