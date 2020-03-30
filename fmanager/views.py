from django.shortcuts import render


def fmanager(request):
    return render(request, 'fmanager/file-manager.html')