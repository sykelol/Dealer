from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import EmailValidator
from phonenumber_field.modelfields import PhoneNumberField
import uuid

# Create your models here.


class Dealership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Broker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CustomerInformation(models.Model):
    first_name = models.CharField(null=True, blank=True, max_length=255)
    last_name = models.CharField(null=True, blank=True, max_length=255)
    date_of_birth = models.DateField(null=True, blank=True,)
    phone_number = PhoneNumberField(null=True, blank=True,)
    email = models.EmailField(null=True, blank=True,)
    address = models.CharField(null=True, blank=True, max_length=255)
    address_line_2 = models.CharField(null=True, blank=True, max_length=255)
    province = models.CharField(null=True, blank=True, max_length=255)
    city = models.CharField(null=True, blank=True, max_length=255)
    postal_code = models.CharField(null=True, blank=True, max_length=255)
    social_insurance_number = models.CharField(null=True, blank=True, max_length=255)
    drivers_license = models.FileField(null=True, blank=True, upload_to='drivers_licenses')
    employment_status = models.CharField(null=True, blank=True, max_length=255)
    company_name = models.CharField(null=True, blank=True, max_length=255)
    job_title = models.CharField(null=True, blank=True, max_length=255)
    employment_length = models.CharField(null=True, blank=True, max_length=255)
    salary = models.CharField(null=True, blank=True, max_length=255)
    monthly_income = models.CharField(null=True, blank=True, max_length=255)
    other_income = models.CharField(null=True, blank=True, max_length=255)
    paystub_file = models.FileField(null=True, blank=True, upload_to='paystubs')
    tax_return = models.FileField(null=True, blank=True, upload_to='tax_returns')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

class VehicleInformation(models.Model):
    Dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE, blank=True, null=True)
    customer = models.OneToOneField(CustomerInformation, on_delete=models.CASCADE)
    vinNumber = models.CharField(null=True, blank=True, max_length = 100)
    stockNumber = models.IntegerField(null=True, blank=True)
    vehiclePrice = models.IntegerField(null=True, blank=True,)
    downPayment = models.IntegerField(null=True, blank=True)
    vehicleMileage = models.IntegerField(null=True, blank=True,)
    make = models.CharField(null=True, blank=True, max_length = 100)
    model = models.CharField(null=True, blank=True, max_length = 100)
    trim = models.CharField(null=True, blank=True, max_length = 100)
    year = models.IntegerField(null=True, blank=True,)
    color = models.CharField(null=True, blank=True, max_length = 100)
    status = models.CharField(null=True, blank=True, max_length=100, default='pending')
    
    tradeInVin = models.CharField(max_length=100, null=True, blank=True)
    tradeInPrice = models.IntegerField(null=True, blank=True)
    tradeInMileage = models.IntegerField(null=True, blank=True)
    tradeInMake = models.CharField(max_length=100, null=True, blank=True)
    tradeInModel = models.CharField(max_length=100, null=True, blank=True)
    tradeInTrim = models.CharField(max_length=100, null=True, blank=True)
    tradeInYear = models.CharField(max_length=100, null=True, blank=True)
    tradeInColor = models.CharField(max_length=100, null=True, blank=True)

    vehicleFront = models.FileField(null=True, blank=True, upload_to='vehicle_front')
    vehicleSide = models.FileField(null=True, blank=True, upload_to='vehicle_side')
    vehicleBack = models.FileField(null=True, blank=True, upload_to='vehicle_back')
    vehicleOdometer = models.FileField(null=True, blank=True, upload_to='vehicle_odometer')
    vehicleInterior = models.FileField(null=True, blank=True, upload_to='vehicle_interior')
    exampleDocument1 = models.FileField(null=True, blank=True, upload_to='example_document1')
    exampleDocument2 = models.FileField(null=True, blank=True, upload_to='example_document2')

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']


#class VehiclePictures(models.Model):
    #front_view = models.ImageField(upload_to='get_upload_to', max_length=200, )
