from django.shortcuts import render
from settings.models import Playgrounds
from logpage.models import Profile


def playgrounds(request):
    playgrounds = Playgrounds.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'playgrounds/playgrounds.html', {'playgrounds': playgrounds, 'typeuser': typeuser})
    else:
        return render(request, 'playgrounds/playgrounds.html', {'playgrounds': playgrounds})
