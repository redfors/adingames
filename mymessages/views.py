from django.shortcuts import render
from .models import Mymessages


def mymessages(request):
    mymessages = Mymessages.objects.all()
    return render(request, 'mymessages/mymessages.html', {'mymessages': mymessages})
