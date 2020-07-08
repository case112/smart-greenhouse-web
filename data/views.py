from django.shortcuts import render
import datetime
from django.http import JsonResponse
from . models import State, Sensor, Object


def index(request):
    latest_sensors = Sensor.objects.all().order_by('-created_at')[:10]
    latest_states = State.objects.all().order_by('-created_at')[:10]
    window_state1 = State.objects.filter(state_name=8).order_by('-created_at').first()
    window_state2 = State.objects.filter(state_name=9).order_by('-created_at').first()
    voltage = State.objects.filter(state_name=10).order_by('-created_at').first()
    charge = State.objects.filter(state_name=11).order_by('-created_at').first()
    context = {
		'latest_sensors': latest_sensors,
        'latest_states': latest_states,
        'window_state1': window_state1,
        'window_state2': window_state2,
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