from django.shortcuts import render
from settings.models import Playgrounds


def playgrounds(request):
    playgrounds = Playgrounds.objects.all()
    return render(request, 'playgrounds/playgrounds.html', {'playgrounds': playgrounds})
