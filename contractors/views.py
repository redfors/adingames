from django.shortcuts import render
from .models import Contractors
from logpage.models import Profile

def contractors(request):
    contractors = Contractors.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'contractors/contractors.html', {'contractors': contractors, 'typeuser': typeuser})
    else:
        return render(request, 'contractors/contractors.html', {'contractors': contractors})
