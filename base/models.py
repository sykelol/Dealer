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
    phone_number = models.CharField(null=True, blank=True, max_length=255)
    address = models.CharField(null=True, blank=True, max_length=255)
    address_line_2 = models.CharField(null=True, blank=True, max_length=255)
    province = models.CharField(null=True, blank=True, max_length=255)
    city = models.CharField(null=True, blank=True, max_length=255)
    postal_code = models.CharField(null=True, blank=True, max_length=255)
    drivers_license = models.FileField(null=True, blank=True, upload_to='drivers_licenses')
    employment_status = models.CharField(null=True, blank=True, max_length=255)
    company_name = models.CharField(null=True, blank=True, max_length=255)
    job_title = models.CharField(null=True, blank=True, max_length=255)
    employment_length = models.CharField(null=True, blank=True, max_length=255)
    salary = models.CharField(null=True, blank=True, max_length=255)
    monthly_income = models.CharField(null=True, blank=True, max_length=255)
    other_income = models.CharField(null=True, blank=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    is_customer = models.BooleanField(default=False)
    is_dealer = models.BooleanField(default=False)
    is_broker = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    dealer_name = models.CharField(null=True, blank=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

"""
    def save(self, *args, **kwargs):
        # hash password before saving user
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
"""
        
class CustomerVehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    make = models.CharField(null=True, blank=True, max_length = 100)
    model = models.CharField(null=True, blank=True, max_length = 100)
    year = models.CharField(null=True, blank=True, max_length = 100)
    down_payment = models.CharField(null=True, blank=True, max_length = 100)
    vinNumber = models.CharField(null=True, blank=True, max_length = 100)
    stockNumber = models.CharField(null=True, blank=True, max_length = 100)
    vehiclePrice = models.CharField(null=True, blank=True, max_length = 100)
    vehicleMileage = models.CharField(null=True, blank=True, max_length = 100)
    trim = models.CharField(null=True, blank=True, max_length = 100)
    color = models.CharField(null=True, blank=True, max_length = 100)
    status = models.CharField(null=True, blank=True, max_length=100, default='pending')
    
    tradeInVin = models.CharField(max_length=100, null=True, blank=True)
    tradeInPrice = models.CharField(null=True, blank=True, max_length = 100)
    tradeInMileage = models.CharField(null=True, blank=True, max_length = 100)
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
        return self.make



"""
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

"""
"""
class User(AbstractUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        CUSTOMER = "CUSTOMER", 'Customer'
        DEALER = "DEALER", 'Dealer'
    
    base_role = Role.ADMIN

    role = models.CharField(max_length=255, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

class Customer(User):
    base_role = User.Role.CUSTOMER

    class meta:
        proxy = True

@receiver(post_save, sender=Customer)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CUSTOMER":
        CustomerProfile.objects.create(user=instance)

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_line_2 = models.CharField(null=True, blank=True, max_length=255)
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    drivers_license = models.FileField(null=True, blank=True, upload_to='drivers_licenses')
    employment_status = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    employment_length = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    monthly_income = models.CharField(max_length=255)
    other_income = models.CharField(null=True, blank=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True)

class DealerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, unique=True)
    dealer_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_line_2 = models.CharField(null=True, blank=True, max_length=255)
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

class Dealer(User):
    base_role = User.Role.DEALER

    class meta:
        proxy = True
"""
"""
class CustomerUser(AbstractBaseUser, PermissionsMixin):

    groups = models.ManyToManyField(
        to='auth.Group',
        related_name='customer_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        to='auth.Permission',
        related_name='customer_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_line_2 = models.CharField(null=True, blank=True, max_length=255)
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    drivers_license = models.FileField(null=True, blank=True, upload_to='drivers_licenses')
    employment_status = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    employment_length = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    monthly_income = models.CharField(max_length=255)
    other_income = models.CharField(null=True, blank=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'address', 'province', 'city', 'postal_code', 'drivers_license',
                       'employment_status', 'company_name', 'job_title', 'employment_length', 'salary', 'monthly_income', 'other_income']

    objects = UserManager()

    def __str__(self):
        return self.email

class DealerUser(AbstractBaseUser, PermissionsMixin):

    groups = models.ManyToManyField(
        to='auth.Group',
        related_name='dealer_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        to='auth.Permission',
        related_name='dealer_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    email = models.EmailField(max_length=255, unique=True)
    dealer_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_line_2 = models.CharField(null=True, blank=True, max_length=255)
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['dealer_name', 'phone_number', 'address', 'province', 'city', 'postal_code']

    objects = UserManager()

    def __str__(self):
        return self.email

class SuperUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=30, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=True)
    is_superuser = models.BooleanField(_('superuser status'), default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        verbose_name = _('superuser')
        verbose_name_plural = _('superusers')

    def __str__(self):
        return self.email
"""

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

    Dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE, blank=True, null=True)
    vinNumber = models.CharField(null=True, blank=True, max_length = 100)
    stockNumber = models.CharField(null=True, blank=True, max_length = 100)
    vehiclePrice = models.CharField(null=True, blank=True, max_length = 100)
    downPayment = models.CharField(null=True, blank=True, max_length = 100)
    vehicleMileage = models.CharField(null=True, blank=True, max_length = 100)
    make = models.CharField(null=True, blank=True, max_length = 100)
    model = models.CharField(null=True, blank=True, max_length = 100)
    trim = models.CharField(null=True, blank=True, max_length = 100)
    year = models.CharField(null=True, blank=True, max_length = 100)
    color = models.CharField(null=True, blank=True, max_length = 100)
    status = models.CharField(null=True, blank=True, max_length=100, default='pending')
    
    tradeInVin = models.CharField(max_length=100, null=True, blank=True)
    tradeInPrice = models.CharField(null=True, blank=True, max_length = 100)
    tradeInMileage = models.CharField(null=True, blank=True, max_length = 100)
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
