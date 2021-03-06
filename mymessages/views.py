from django.shortcuts import render
from .models import Mymessages
from logpage.models import Profile

def mymessages(request):
    messages = Mymessages.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'mymessages/messages.html', {'messages': messages, 'typeuser': typeuser})
    else:
        return render(request, 'mymessages/messages.html', {'messages': messages})
