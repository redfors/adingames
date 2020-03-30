from django.shortcuts import render


def mycalendar(request):
    return render(request, 'mycalendar/calendar.html')