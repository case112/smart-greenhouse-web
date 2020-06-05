from django.db import models

# New model that combines all sensors
class Sensors(models.Model):
    name = models.ForeignKey(to=Objects, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    temperature = models.CharField(max_length=5, blank=True)
    humidity = models.CharField(max_length=5, blank=True)
    moisture = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.name

    @property
    def sensor_id(self):
        return self.id

# New model that lets define names(of devices)
class Objects(models.Model):
    object_name = models.CharField(max_length=30)

    def __str__(self):
        return self.object_name

# New model that combines State/Voltage/Charge
class States(models.Model):
    name = models.ForeignKey(to=Objects, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    state = models.BooleanField()
    value = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name

    @property
    def sensor_id(self):
        return self.id


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