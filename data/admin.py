from django.contrib import admin

from . models import Dht22, Chirp, WindowState, Voltage, Charge, Sensor, Object, State

class SensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_name', 'temperature', 'humidity', 'moisture', 'date')
    list_filter = ('date',)

class ObjectAdmin(admin.ModelAdmin):
    list_display = ('object_name',)

class StateAdmin(admin.ModelAdmin):
    list_display = ('state_name', 'state', 'value', 'date')
    list_filter = ('date',)

class Dht22Admin(admin.ModelAdmin):
    list_display = ('sensor', 'temperature', 'humidity', 'date')
    list_filter = ('date',)

class ChirpAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'moisture_value', 'moisture', 'temperature', 'date')
    list_filter = ('date',)

class WindowStateAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'state', 'date')
    list_filter = ('date',)

class VoltageAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'volts', 'date')
    list_filter = ('date',)

class ChargeAdmin(admin.ModelAdmin):
    list_display = ('charger', 'state', 'date')
    list_filter = ('date',)

admin.site.register(Dht22, Dht22Admin)
admin.site.register(Chirp, ChirpAdmin)
admin.site.register(WindowState, WindowStateAdmin)
admin.site.register(Voltage, VoltageAdmin)
admin.site.register(Charge, ChargeAdmin)

admin.site.register(Sensor, SensorAdmin)
admin.site.register(Object, ObjectAdmin)
admin.site.register(State, StateAdmin)

