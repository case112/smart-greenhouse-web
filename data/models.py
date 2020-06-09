from django.db import models

# New model that lets define names(of devices)
class Object(models.Model):
    object_name = models.CharField(max_length=30)

    def __str__(self):
        return self.object_name


# New model that combines all sensors
class Sensor(models.Model):
    sensor_name = models.ForeignKey(Object, on_delete=models.PROTECT, related_name='sensor_name')
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    temperature = models.CharField(max_length=5, blank=True, null=True)
    humidity = models.CharField(max_length=5, blank=True, null=True)
    moisture = models.CharField(max_length=5, blank=True, null=True)

    #def __str__(self):
        #return self.sensor_name

    #@property
    #def sensor_id(self):
        #return self.id

# New model that combines State/Voltage/Charge
class State(models.Model):
    state_name = models.ForeignKey(Object, on_delete=models.PROTECT, related_name='state_name')
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    state = models.BooleanField()
    value = models.CharField(max_length=10, blank=True, null=True)

    #def __str__(self):
       # return self.state_name

    #@property
    #def sensor_id(self):
        #return self.id


# Older models ----------------------

class Dht22(models.Model):
    sensor = models.CharField(max_length=20)
    temperature = models.CharField(max_length=5)
    humidity = models.CharField(max_length=5)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.sensor

    @property
    def dht22_id(self):
        return self.id


class Chirp(models.Model):
    sensor = models.CharField(max_length=20)
    moisture_value = models.CharField(max_length=3)
    moisture = models.CharField(max_length=5)
    temperature = models.CharField(max_length=5)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.sensor


class WindowState(models.Model):
    sensor = models.CharField(max_length=20)
    state = models.BooleanField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.sensor


class Voltage(models.Model):
    sensor = models.CharField(max_length=20)
    volts = models.CharField(max_length=5)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.sensor


class Charge(models.Model):
    charger = models.CharField(max_length=20)
    state = models.BooleanField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.charger