from django.shortcuts import render
from logpage.models import Profile
from django.http import HttpResponse

def dashaboard(request):
    if request.is_ajax():
        typeUser = request.GET.get('typeUser')
        user = request.user

        type = Profile.objects.get(user=user)
        type.type_user = typeUser

        type.save()

    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'dashboard/index.html', {'typeuser': typeuser})
    else:
        return render(request, 'dashboard/index.html')
