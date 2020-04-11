from django.shortcuts import render
from .models import Newspage


def newspage(request):
    newspage = Newspage.objects.all()
    return render(request, 'newspage/newspage.html', {'newspage': newspage})
