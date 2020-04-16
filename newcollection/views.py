from django.shortcuts import render
from logpage.models import Profile


def newcollection(request):
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)

        return render(request, 'newcollection/newcollection.html', {'typeuser': typeuser})
    else:
        return render(request, 'newcollection/newcollection.html')
