from django.shortcuts import render


def logpage(request):
    return render(request, 'logpage/login.html')