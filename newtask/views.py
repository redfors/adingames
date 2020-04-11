from django.shortcuts import render


def newtask(request):

    return render(request, 'newtask/newtask.html')
