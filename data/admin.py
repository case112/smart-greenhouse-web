from django.contrib import admin

from . models import Sensor, Object, State, Log

class SensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_name', 'temperature', 'humidity', 'moisture', 'created_at')
    list_filter = ('created_at',)

class ObjectAdmin(admin.ModelAdmin):
    list_display = ('object_name',)

class StateAdmin(admin.ModelAdmin):
    list_display = ('state_name', 'state', 'value', 'created_at')
    list_filter = ('created_at',)

class LogAdmin(admin.ModelAdmin):
    list_display = ('logger', 'level', 'trace', 'msg', 'created_at')
    list_filter = ('created_at',)


admin.site.register(Sensor, SensorAdmin)
admin.site.register(Object, ObjectAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Log, LogAdmin)

