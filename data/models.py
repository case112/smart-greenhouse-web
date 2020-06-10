from django.db import models

# Combines names(of devices)
class Object(models.Model):
    object_name = models.CharField(max_length=30)

    def __str__(self):
        return self.object_name


# Combines all sensors
class Sensor(models.Model):
    sensor_name = models.ForeignKey(Object, on_delete=models.PROTECT, related_name='sensor_name')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    temperature = models.CharField(max_length=5, blank=True, null=True)
    humidity = models.CharField(max_length=5, blank=True, null=True)
    moisture = models.CharField(max_length=5, blank=True, null=True)


# Combines State/Voltage/Charge
class State(models.Model):
    state_name = models.ForeignKey(Object, on_delete=models.PROTECT, related_name='state_name')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    state = models.BooleanField()
    value = models.CharField(max_length=10, blank=True, null=True)

    
class Log(models.Model):
    logger = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    trace = models.TextField()
    msg = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)