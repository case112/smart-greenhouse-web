from django.shortcuts import render
import datetime
from django.http import JsonResponse
from . models import State, Sensor, Object


def index(request):
    latest = Sensor.objects.all().order_by('-created_at')[:10]
    window_state = State.objects.all().latest('created_at')
    voltage = State.objects.all().latest('created_at')
    charge = State.objects.all().latest('created_at')
    context = {
		'latest': latest,
        'window_state': window_state,
        'voltage': voltage,
        'charge': charge,
	}
    return render(request, 'index.html', context)


# def temp_today(request):
#     time = []
#     data = []
#     queryset = Dht22.objects.filter(sensor__exact='Greenhouse2').order_by('-date')[:16][::-1]
#     for entry in queryset:
#         x = str(entry.date)
#         time.append(x[11:-3])
#         data.append(entry.temperature)
#     return JsonResponse(data={
#         'time': time,
#         'data': data,
#     })

# def hum_today(request):
#     time = []
#     data = []
#     queryset = Dht22.objects.filter(sensor__exact='Greenhouse2').order_by('-date')[:16][::-1]
#     for entry in queryset:
#         x = str(entry.date)
#         time.append(x[11:-3])
#         data.append(entry.humidity)
#     return JsonResponse(data={
#         'time': time,
#         'data': data,
#     })