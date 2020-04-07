from django.contrib import admin

from . models import Dht22, Chrip

class Dht22Admin(admin.ModelAdmin):
    list_display = ('sensor', 'temperature', 'humidity', 'date')
    list_filter = ('date',)

class ChirpAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'moisture_value', 'moisture', 'temperature', 'date')
    list_filter = ('date',)

admin.site.register(Dht22, Dht22Admin)
admin.site.register(Chrip, ChirpAdmin)

