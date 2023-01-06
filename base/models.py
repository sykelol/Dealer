from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import EmailValidator
from phonenumber_field.modelfields import PhoneNumberField

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
    status_choices = [    ('pending', 'Pending'),    ('approved', 'Approved'),    ('declined', 'Declined'),]
    status = models.CharField(max_length=100, default='pending', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.vinNumber

class CustomerInformation(models.Model):
    vehicle = models.OneToOneField(VehicleInformation, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(max_length=100)
    phone_number = PhoneNumberField(max_length=15)
    email = models.EmailField(unique=True, validators=[EmailValidator])
    address = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    social_insurance_number = models.CharField(max_length=9)
    employment_status = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    employment_length = models.PositiveIntegerField()
    salary = models.PositiveIntegerField()
    monthly_income = models.PositiveIntegerField()
    other_income = models.PositiveIntegerField(blank=True)
    paystub_file = models.FileField(upload_to='pay_stubs/', blank=True, null=True)
    tax_return = models.FileField(upload_to='tax_returns/', blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']


# class EmploymentInformation(models.Model):
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE, null=True, blank=True)
    # company_name = models.CharField(max_length=100)
    # job_title = models.CharField(max_length=100)
    # salary = models.PositiveIntegerField()


# class Customer(models.Model):
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # email = models.EmailField(unique=True)
    # phone_number = models.CharField(max_length=20)
