from django.shortcuts import render
from .models import Statistic
from logpage.models import Profile


def statistic(request):
    statistic = Statistic.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'statistic/statistic.html', {'statistic': statistic, 'typeuser': typeuser})
    else:
        return render(request, 'statistic/statistic.html', {'statistic': statistic})
