from django.shortcuts import render
import datetime
from django.http import JsonResponse
from . models import Dht22


def index(request):
    latest = Dht22.objects.all()[:7][::-1]
    context = {
		'latest': latest,
	}
    return render(request, 'index.html', context)


def temp_today(request):
    time = []
    data = []
    queryset = Dht22.objects.filter(sensor__exact='Greenhouse2').order_by('-date')[:16][::-1]
    for entry in queryset:
        x = str(entry.date)
        time.append(x[11:-3])
        data.append(entry.temperature)
    return JsonResponse(data={
        'time': time,
        'data': data,
    })

def hum_today(request):
    time = []
    data = []
    queryset = Dht22.objects.filter(sensor__exact='Greenhouse2').order_by('-date')[:16][::-1]
    for entry in queryset:
        x = str(entry.date)
        time.append(x[11:-3])
        data.append(entry.humidity)
    return JsonResponse(data={
        'time': time,
        'data': data,
    })