from django.shortcuts import render
from .models import Mycollections


def mycollections(request):
    mycollections = Mycollections.objects.all()
    return render(request, 'mycollections/mycollections.html', {'mycollections': mycollections})
