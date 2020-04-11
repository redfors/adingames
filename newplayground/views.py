from django.shortcuts import render



def newplayground(request):

    return render(request, 'newplayground/newplayground.html')
