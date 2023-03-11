from django.contrib import admin
# Register your models here.

from .models import VehicleInformation, Dealership, Broker, User, CustomerVehicle
from file_resubmit.admin import AdminResubmitMixin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password

class VehicleInformationAdmin(AdminResubmitMixin, admin.ModelAdmin):
    pass

class CustomerInformationAdmin(AdminResubmitMixin, admin.ModelAdmin):
    pass

class CustomAdmin(UserAdmin):
    model = User
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'phone_number')}),
        ('Address info', {'fields': ('address', 'address_line_2', 'province', 'city', 'postal_code')}),
        ('Employment info', {'fields': ('employment_status', 'company_name', 'job_title', 'employment_length', 'salary', 'monthly_income', 'other_income')}),
        ('Permissions', {'fields': ('is_active', 'is_customer', 'is_dealer', 'is_broker', 'is_staff', 'dealer_name')}),
    )
    ordering = ('id',)
    list_display = ('id', 'email',)

admin.site.register(VehicleInformation, VehicleInformationAdmin)
admin.site.register(Dealership)
admin.site.register(Broker)
admin.site.register(User, CustomAdmin)
admin.site.register(CustomerVehicle)
'''admin.site.register(CustomerInformation, CustomerInformationAdmin)'''