from django.shortcuts import render
from .models import Contractors


def contractors(request):
    contractors = Contractors.objects.all()
    return render(request, 'contractors/contractors.html', {'contractors': contractors})
