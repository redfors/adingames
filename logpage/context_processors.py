from .models import Profile

def typeUser(request):

    return {'typeuser': Profile.objects.filter(user=request.user)}