from django.shortcuts import render
from .models import Newspage
from logpage.models import Profile


def newspage(request):
    newspage = Newspage.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'newspage/newspage.html', {'newspage': newspage, 'typeuser': typeuser})
    else:
        return render(request, 'newspage/newspage.html', {'newspage': newspage})
