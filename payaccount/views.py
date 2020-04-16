from django.shortcuts import render
from .models import PayAccount
from logpage.models import Profile

def payaccount(request):
    payaccount = PayAccount.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'payaccount/payaccount.html', {'payaccount': payaccount, 'typeuser': typeuser})
    else:
        return render(request, 'payaccount/payaccount.html')

