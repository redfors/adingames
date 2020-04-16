from django.shortcuts import render
from logpage.models import Profile


def dashaboard(request):
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'dashboard/index.html', {'typeuser': typeuser})
    else:
        return render(request, 'dashboard/index.html')
