from django.shortcuts import render
from logpage.models import Profile


def newcard(request):
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'newcard/newcard.html', {'typeuser': typeuser})
    else:
        return render(request, 'newcard/newcard.html')
