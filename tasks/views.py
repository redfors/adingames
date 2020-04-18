from django.shortcuts import render, redirect
from .models import Tasks
from logpage.models import Profile
from tasks.forms import TasksForm


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

def newtask(request):
    if request.method == 'POST':
        form = TasksForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/')
    else:
        form = TasksForm()

    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'tasks/newtask.html', {'form': form, 'typeuser': typeuser})
    else:
        return render(request, 'tasks/newtask.html', {'form': form})