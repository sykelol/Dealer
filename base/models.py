from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class VehicleInformation(models.Model):
    vinNumber = models.CharField(max_length = 100)
    stockNumber = models.IntegerField(null=True, blank=True)
    vehiclePrice = models.IntegerField()
    downPayment = models.IntegerField(null=True, blank=True)
    tradeInPrice = models.IntegerField(null=True, blank=True)
    vehicleMileage = models.IntegerField()
    make = models.CharField(max_length = 100)
    model = models.CharField(max_length = 100)
    trim = models.CharField(max_length = 100)
    year = models.IntegerField()
    color = models.CharField(max_length = 100)
    fuelType = models.CharField(max_length = 100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.vinNumber
