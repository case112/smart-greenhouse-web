from django.contrib import admin

from . models import Dht22

class Dht22Admin(admin.ModelAdmin):
    list_display = ('sensor', 'temperature', 'humidity', 'date')
    list_filter = ('date',)

admin.site.register(Dht22, Dht22Admin)
