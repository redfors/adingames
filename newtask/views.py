from django.shortcuts import render, redirect
from newtask.forms import TasksForm
from logpage.models import Profile

def newtasks(request):
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
        return render(request, 'newtask/newtask.html', {'form': form, 'typeuser': typeuser})
    else:
        return render(request, 'newtask/newtask.html', {'form': form})


