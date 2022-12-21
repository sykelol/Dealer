from django.contrib import admin

# Register your models here.

from .models import VehicleInformation, Dealership, Broker

admin.site.register(VehicleInformation)
admin.site.register(Dealership)
admin.site.register(Broker)