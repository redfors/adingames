from django.shortcuts import render



def newcard(request):

    return render(request, 'newcard/newcard.html')
