from django.db import models


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