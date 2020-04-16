from django.shortcuts import render

from logpage.models import Profile


def settings(request):
    profile = Profile.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'settings/settings.html', {'profile': profile, 'typeuser': typeuser})
    else:
        return render(request, 'settings/settings.html', {'profile': profile})