from django.shortcuts import render
from .models import Mytools
from logpage.models import Profile


def mytools(request):
    tools = Mytools.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'mytools/tools.html', {'tools': tools, 'typeuser': typeuser})
    else:
        return render(request, 'mytools/tools.html', {'tools': tools})
