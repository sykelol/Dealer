from django.db import models
#from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import EmailValidator
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from virtualcargeeks.storage_backends import PrivateS3Boto3Storage

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.password = make_password(password)
        try:
            user.full_clean()  # Check for validation errors
        except ValidationError as e:
            raise ValueError(str(e))
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(null=True, blank=True, max_length=155)
    last_name = models.CharField(null=True, blank=True, max_length=155)
    date_of_birth = models.CharField(null=True, blank=True, max_length=255)
    phone_number = models.CharField(null=True, blank=True, max_length=100)
    address = models.CharField(null=True, blank=True, max_length=255)
    address_line_2 = models.CharField(null=True, blank=True, max_length=255)
    province = models.CharField(null=True, blank=True, max_length=255)
    city = models.CharField(null=True, blank=True, max_length=255)
    postal_code = models.CharField(null=True, blank=True, max_length=255)
    drivers_license = models.FileField(null=True, blank=True, upload_to='vehicles', storage=PrivateS3Boto3Storage())
    employment_status = models.CharField(null=True, blank=True, max_length=255)
    company_name = models.CharField(null=True, blank=True, max_length=255)
    job_title = models.CharField(null=True, blank=True, max_length=255)
    employment_length = models.CharField(null=True, blank=True, max_length=255)
    salary = models.IntegerField(null=True, blank=True, default=0, validators=[MaxValueValidator(10000000), MinValueValidator(0)])
    monthly_income = models.IntegerField(null=True, blank=True, default=0, validators=[MaxValueValidator(10000000), MinValueValidator(0)])
    other_income = models.IntegerField(null=True, blank=True, default=0, validators=[MaxValueValidator(10000000), MinValueValidator(0)])
    created = models.DateTimeField(auto_now_add=True)
    is_customer = models.BooleanField(default=False)
    is_dealer = models.BooleanField(default=False)
    is_broker = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    tax_return = models.FileField(null=True, blank=True, upload_to='tax_return')
    paystub = models.FileField(null=True, blank=True, upload_to='paystub')
    additional_documents = models.FileField(null=True, blank=True, upload_to='additional_documents')
    
    dealer_name = models.CharField(null=True, blank=True, max_length=255)
    dealer = models.ForeignKey('Dealer', null=True, blank=True, on_delete=models.SET_NULL, related_name='customers')
    created = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_financing_form_url(self):
        base_url = 'http://127.0.0.1:8000'  # Your website's base URL
        return f'{base_url}/dealerlandingpage/{self.id}/'

    def __str__(self):
        if self.dealer_name:
            return self.dealer_name
        else:
            return self.email

class Dealer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dealer_name = models.CharField(null=True, blank=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    # your other fields here

    def __str__(self):
        return self.dealer_name

class CustomerVehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_vehicle')
    created = models.DateTimeField(auto_now_add=True)
    make = models.CharField(null=True, blank=True, max_length = 100)
    model = models.CharField(null=True, blank=True, max_length = 100)
    year = models.CharField(null=True, blank=True, max_length = 100)
    down_payment = models.IntegerField(null=True, blank=True, default=0, validators=[MaxValueValidator(10000000), MinValueValidator(0)])
    vinNumber = models.CharField(null=True, blank=True, max_length = 100)
    stockNumber = models.CharField(null=True, blank=True, max_length = 100)
    vehiclePrice = models.IntegerField(null=True, blank=True, default=0, validators=[MaxValueValidator(10000000), MinValueValidator(0)])
    vehicleMileage = models.IntegerField(null=True, blank=True, default=0, validators=[MaxValueValidator(10000000), MinValueValidator(0)])
    trim = models.CharField(null=True, blank=True, max_length = 100)
    color = models.CharField(null=True, blank=True, max_length = 100)
    dealer = models.CharField(null=True, blank=True, max_length=225)
    dealer_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nondealer_customers', null=True, blank=True)
    status = models.CharField(null=True, blank=True, max_length=100, default='PENDING')
    progress = models.CharField(null=True, blank=True, max_length=225)
    
    tradeInVin = models.CharField(max_length=100, null=True, blank=True)
    tradeInPrice = models.IntegerField(null=True, blank=True, default=0, validators=[MaxValueValidator(10000000), MinValueValidator(0)])
    tradeInMileage = models.IntegerField(null=True, blank=True, default=0, validators=[MaxValueValidator(10000000), MinValueValidator(0)])
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
    

    def __str__(self):
        return self.user.email

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
'''
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
'''

class VehicleInformation(models.Model):
    first_name = models.CharField(null=True, blank=True, max_length=255)
    last_name = models.CharField(null=True, blank=True, max_length=255)
    date_of_birth = models.DateField(null=True, blank=True,)
    phone_number = models.CharField(null=True, blank=True, max_length=100)
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
    salary = models.IntegerField(null=True, blank=True, default=0, validators=[MaxValueValidator(10000000), MinValueValidator(0)])
    monthly_income = models.IntegerField(null=True, blank=True, default=0, validators=[MaxValueValidator(10000000), MinValueValidator(0)])
    other_income = models.IntegerField(null=True, blank=True, default=0, validators=[MaxValueValidator(10000000), MinValueValidator(0)])
    paystub_file = models.FileField(null=True, blank=True, upload_to='paystubs')
    tax_return = models.FileField(null=True, blank=True, upload_to='tax_returns')

    Dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE, blank=True, null=True)
    dealer_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='dealer_submitted_vehicle')
    dealer = models.CharField(null=True, blank=True, max_length=225)
    vinNumber = models.CharField(null=True, blank=True, max_length = 100)
    stockNumber = models.CharField(null=True, blank=True, max_length = 100)
    vehiclePrice = models.IntegerField(null=True, blank=True, default=0, validators=[MaxValueValidator(10000000), MinValueValidator(0)])
    downPayment = models.IntegerField(null=True, blank=True, default=0, validators=[MaxValueValidator(10000000), MinValueValidator(0)])
    vehicleMileage = models.IntegerField(null=True, blank=True, default=0, validators=[MaxValueValidator(10000000), MinValueValidator(0)])
    make = models.CharField(null=True, blank=True, max_length = 100)
    model = models.CharField(null=True, blank=True, max_length = 100)
    trim = models.CharField(null=True, blank=True, max_length = 100)
    year = models.CharField(null=True, blank=True, max_length = 100)
    color = models.CharField(null=True, blank=True, max_length = 100)
    status = models.CharField(null=True, blank=True, max_length=100, default='PENDING')
    progress = models.CharField(null=True, blank=True, max_length=225)
    
    tradeInVin = models.CharField(max_length=100, null=True, blank=True)
    tradeInPrice = models.IntegerField(null=True, blank=True, default=0, validators=[MaxValueValidator(10000000), MinValueValidator(0)])
    tradeInMileage = models.IntegerField(null=True, blank=True, default=0, validators=[MaxValueValidator(10000000), MinValueValidator(0)])
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
