from django.shortcuts import render
from .models import Statistic


def statistic(request):
    statistic = Statistic.objects.all()
    return render(request, 'statistic/statistic.html', {'statistic': statistic})
