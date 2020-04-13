from django.shortcuts import render, redirect
from newtask.forms import TasksForm


def newtasks(request):
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TasksForm()
    return render(request, 'newtask/newtask.html', {'form': form})
