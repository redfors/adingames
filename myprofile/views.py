from django.shortcuts import render

from logpage.models import Profile


def myprofile(request):
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'myprofile/profile.html', {'typeuser': typeuser})
    else:
        return render(request, 'myprofile/profile.html')
