from django.contrib import admin
# Register your models here.

from .models import VehicleInformation, Dealership, Broker
from file_resubmit.admin import AdminResubmitMixin

class VehicleInformationAdmin(AdminResubmitMixin, admin.ModelAdmin):
    pass

class CustomerInformationAdmin(AdminResubmitMixin, admin.ModelAdmin):
    pass

admin.site.register(VehicleInformation, VehicleInformationAdmin)
admin.site.register(Dealership)
admin.site.register(Broker)
'''admin.site.register(CustomerInformation, CustomerInformationAdmin)'''