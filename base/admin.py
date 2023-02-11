from django.contrib import admin
# Register your models here.

from .models import VehicleInformation, Dealership, Broker, CustomerInformation


admin.site.register(VehicleInformation)
admin.site.register(Dealership)
admin.site.register(Broker)
admin.site.register(CustomerInformation)