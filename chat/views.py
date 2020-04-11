from django.shortcuts import render
from .models import Chat


def chat(request):
    tasks = Chat.objects.all()
    return render(request, 'chat/chat.html', {'chat': chat})
