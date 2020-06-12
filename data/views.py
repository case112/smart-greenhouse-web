from django.shortcuts import render
import datetime
from django.http import JsonResponse
from . models import State, Sensor, Object


def index(request):
    latest = Sensor.objects.all().order_by('-created_at')[:10]
    window_state = State.objects.filter(state_name=2).order_by('created_at')
    voltage = State.objects.filter(state_name=1).order_by('created_at')
    charge = State.objects.filter(state_name=3).order_by('created_at')
    context = {
		'latest': latest,
        'window_state': window_state,
        'voltage': voltage,
        'charge': charge,
	}
    return render(request, 'index.html', context)


def temp_today(request):
    time = []
    data = []
    queryset = Sensor.objects.filter(sensor_name=1).order_by('-created_at')[:16][::-1]
    for entry in queryset:
        x = str(entry.created_at)
        time.append(x[11:-3])
        data.append(entry.temperature)
    return JsonResponse(data={
        'time': time,
        'data': data,
    })

def hum_today(request):
    time = []
    data = []
    queryset = Sensor.objects.filter(sensor_name=1).order_by('-created_at')[:16][::-1]
    for entry in queryset:
        x = str(entry.created_at)
        time.append(x[11:-3])
        data.append(entry.humidity)
    return JsonResponse(data={
        'time': time,
        'data': data,
    })