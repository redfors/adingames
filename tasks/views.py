from django.shortcuts import render
from .models import Tasks


def tasks(request):
    tasks = Tasks.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks})
