from django.shortcuts import render


def myprofile(request):

    return render(request, 'myprofile/myprofile.html')
