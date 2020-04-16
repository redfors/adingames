from django.shortcuts import render
from .models import Tasks
from logpage.models import Profile


def tasks(request):
    tasks = Tasks.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'tasks/tasks.html', {'tasks': tasks, 'typeuser': typeuser})
    else:
        return render(request, 'tasks/tasks.html', {'tasks': tasks})

