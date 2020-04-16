from django.shortcuts import render
from .models import Account
from logpage.models import Profile

def account(request):
    account = Account.objects.all()
    if request.user.is_active:
        typeuser = Profile.objects.filter(user=request.user)
        return render(request, 'account/account.html', {'account': account, 'typeuser': typeuser})
    else:
        return render(request, 'account/account.html')

