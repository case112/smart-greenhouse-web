from django.shortcuts import render
import datetime
from django.http import JsonResponse
from . models import Dht22


def index(request):
    return render(request, 'index.html', {})



def temperature_chart(request):
    dates = []
    data = []

    date_from = datetime.datetime.now() - datetime.timedelta(days=1)

    queryset = Dht22.objects.filter(date__gte=date_from, sensor__exact='Greenhouse2')[:16]
    for entry in queryset:
        x = str(entry.date)
        dates.append(x[11:-3])
        data.append(entry.temperature)
    
    return JsonResponse(data={
        'dates': dates,
        'data': data,
    })