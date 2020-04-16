from django.shortcuts import render
from .models import Tasks
from logpage.models import Profile


def mytasks(request):
    tasks = Tasks.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'tasks/tasks.html', {'tasks': tasks, 'typeuser': typeuser})
    else:
        return render(request, 'tasks/tasks.html', {'tasks': tasks})

def feed(request):
    feed = Tasks.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'tasks/tasks.html', {'feed': feed, 'typeuser': typeuser})
    else:
        return render(request, 'tasks/feed.html', {'feed': feed})

