from django.contrib import admin
# Register your models here.

from .models import VehicleInformation, Dealership, Broker, User, CustomerVehicle, Dealer
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
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'phone_number', 'dealer_name')}),
        ('Address info', {'fields': ('address', 'address_line_2', 'province', 'city', 'postal_code')}),
        ('Employment info', {'fields': ('employment_status', 'company_name', 'job_title', 'employment_length', 'salary', 'monthly_income', 'other_income')}),
        ('Permissions', {'fields': ('is_active', 'is_customer', 'is_dealer', 'is_broker', 'is_staff')}),
    )
    ordering = ('id',)
    list_display = ('id', 'email',)

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('dealer_name', 'id', 'created')
    # your other admin options here

    def created(self, obj):
        return obj.created
    created.admin_order_field = 'created'

admin.site.register(VehicleInformation, VehicleInformationAdmin)
admin.site.register(Dealership)
admin.site.register(Broker)
admin.site.register(User, CustomAdmin)
admin.site.register(CustomerVehicle)
'''admin.site.register(CustomerInformation, CustomerInformationAdmin)'''