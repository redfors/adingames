from django.shortcuts import render
from .models import Chat
from logpage.models import Profile

def chat(request):
    chat = Chat.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'chat/chat.html', {'chat': chat, 'typeuser': typeuser})
    else:
        return render(request, 'chat/chat.html', {'chat': chat})
