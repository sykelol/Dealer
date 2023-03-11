from .models import VehicleInformation, User, CustomerVehicle
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from django.forms import DateInput
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from formtools.wizard.views import SessionWizardView
from django.core.cache import cache
from file_resubmit.admin import AdminResubmitImageWidget, AdminResubmitFileWidget
from django.forms.widgets import ClearableFileInput, PasswordInput
from file_resubmit.admin import ResubmitFileWidget
from django.contrib.auth.forms import UserCreationForm


PROVINCES = (
    ('ON', 'Ontario'),
    ('AB', 'Alberta'),
    ('BC', 'British Columbia'),
    ('MB', 'Manitoba'),
    ('NB', 'New Brunswick'),
    ('NL', 'Newfoundland and Labrador'),
    ('NS', 'Nova Scotia'),
    ('NT', 'Northwest Territories'),
    ('NU', 'Nunavut'),
    ('PE', 'Prince Edward Island'),
    ('QC', 'Quebec'),
    ('SK', 'Saskatchewan'),
    ('YT', 'Yukon'),
)

class CustomerCreationFormOne(UserCreationForm):
    email = forms.EmailField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'example@example.com'})
        )
    is_customer = forms.BooleanField(
        initial=True,
        required=False,
        widget=forms.CheckboxInput(attrs={'id': 'user-type'}),
        label='Is Customer',
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_customer'].disabled = True

    class Meta:
        model = User
        fields=['email', 'password1', 'password2', 'is_customer']


class CustomerCreationFormTwo(ModelForm):
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'First Name'})
        )
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Last Name'})
        )
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'customer-form-field',
            'type': 'date'
        }))
    phone_number = PhoneNumberField(
        required=False,
        label= 'Phone number: (123)-456-7890',
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': '(xxx)-xxx-xxxx'})
        )
    address = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Address'})
        )
    address_line_2 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Apt, suite, etc, (optional)'})
        )
    province = forms.ChoiceField(
        required=False,
        choices=PROVINCES,
        widget=forms.Select(attrs={
            'class': 'customer-form-field-widget',})
        )
    city = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'City'})
        )
    postal_code = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Postal Code'})
        )
    drivers_license = forms.FileField(
        required=False,
        widget=AdminResubmitFileWidget(attrs={'class': 'employment-form-file', 'id': 'drivers_license'})
        )
    
    class Meta:
        model = User
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'customer-form-field', 'required': 'False'}),
            'last_name': forms.TextInput(attrs={'class': 'customer-form-field', 'required': 'False'}),
            'phone_number': forms.TextInput(attrs={'class': 'customer-form-field', 'required': 'False'}),
            'email': forms.TextInput(attrs={'class': 'customer-form-field', 'required': 'False'}),
            'address': forms.TextInput(attrs={'class': 'customer-form-field', 'required': 'False'}),
            'address_line_2': forms.TextInput(attrs={'class': 'customer-form-field', 'required': 'False'}),
            'province': forms.Select(attrs={'class': 'customer-form-field-widget', 'required': 'False'}),
            'city': forms.TextInput(attrs={'class': 'customer-form-field', 'required': 'False'}),
            'postal_code': forms.TextInput(attrs={'class': 'customer-form-field', 'required': 'False'}),
        }
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'address', 'address_line_2', 'province', 'city', 'postal_code', 'drivers_license', 'is_customer']
        
        labels = {
            'first_name': ('First Name'),
            'last_name': ('Last Name'),
            'date_of_birth': ('Date of Birth'),
            'phone_number': ('Phone Number (xxx)-xxx-xxxx'),
            'email': ('Email'),
            'address': ('Address'),
            'address_line_2': ('Address Line 2'),
            'city': ('City'),
            'postal_code': ('Postal Code'),
            'drivers_license': ('Drivers License'),
        }

EMPLOYMENT = (
    ('employed', 'Employed'),
    ('self-employed', 'Self-employed'),
    ('unemployed', 'Unemployed'),
)

class CustomerCreationFormThree(ModelForm):
    employment_status = forms.ChoiceField(
        required=False,
        label= 'Employment status',
        choices=EMPLOYMENT,
        widget=forms.Select(attrs={'class': 'customer-form-field-widget'})
    )
    company_name = forms.CharField(
        required=False,
        label= 'Company name',
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Company Name'})
    )
    job_title = forms.CharField(
        required=False,
        label= 'Job title',
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Job Title'})
    )
    employment_length = forms.CharField(
        required=False,
        label= 'Employment length',
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Employment Length'})
    )
    salary = forms.CharField(
        required=False,
        label = 'Salary',
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Salary'})
    )
    monthly_income = forms.CharField(
        required=False,
        label= 'Monthly income',
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Monthly Income'})
    )
    other_income = forms.CharField(
        required=False,
        label= 'Other income',
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Other Income'})
    )
    
    class Meta:
        model = User
        exclude = ['password1']
        fields = ['employment_status', 'company_name', 'job_title', 'employment_length', 'salary', 'monthly_income', 'other_income']
        labels = {
            'employment_status': 'Employment Status',
            'company_name': 'Company Name',
            'job_title': 'Job Title',
            'employment_length': 'Employment Length',
            'salary': 'Salary',
            'monthly_income': 'Monthly Income',
            'other_income': 'Other Income',
        }

STATUSCHOICES = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('declined', 'Declined'),
]

class CustomerVehicleInfo(ModelForm):
        vinNumber = forms.CharField(
            required=False, label='VIN Number',
            widget=forms.TextInput(attrs={'class': 'customer-form-field'})
        )
        stockNumber = forms.CharField(
            required=False, label='Stock Number',
            widget=forms.TextInput(attrs={'class': 'customer-form-field'})
        )
        vehiclePrice = forms.CharField(
            required=False, label='Vehicle Price',
            widget=forms.TextInput(attrs={'class': 'customer-form-field'})    
        )
        down_payment = forms.CharField(
            required=False, label='Down Payment',
            widget=forms.TextInput(attrs={'class': 'customer-form-field'})
        )
        vehicleMileage = forms.CharField(
            required=False, label='Vehicle Mileage',
            widget=forms.TextInput(attrs={'class': 'customer-form-field'})
        )
        make = forms.CharField(
            required=False, label='Make',
            widget=forms.TextInput(attrs={'class': 'customer-form-field'})
        )
        model = forms.CharField(
            required=False, label='Model',
            widget=forms.TextInput(attrs={'class': 'customer-form-field'})
        )
        trim = forms.CharField(
            required=False, label='Trim',
            widget=forms.TextInput(attrs={'class': 'customer-form-field'})
        )
        year = forms.CharField(
            required=False, label='Year',
            widget=forms.TextInput(attrs={'class': 'customer-form-field'})
        )
        color = forms.CharField(
            required=False, label='Color',
            widget=forms.TextInput(attrs={'class': 'customer-form-field'})
        )
        status = forms.ChoiceField(
            choices=STATUSCHOICES,
            required=False,
            label='Status',
            widget=forms.Select(attrs={'class': 'customer-form-field-widget'})
        )
    
        class Meta:
            model = CustomerVehicle
            fields = ['vinNumber', 'stockNumber', 'vehiclePrice', 'down_payment', 'vehicleMileage', 'make', 'model', 'trim', 'year', 'color', 'status']

class UpdateStatusForm(forms.ModelForm):
    status = forms.ChoiceField(
            choices=STATUSCHOICES,
            required=False,
            label='Status',
            widget=forms.Select(attrs={'class': 'customer-form-field-widget'})
        )
    class Meta:
        model = CustomerVehicle
        fields = ['status']


class DealerRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'example@example.com'})
        )
    dealer_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Dealer name'})
        )
    phone_number = PhoneNumberField(
        required=False,
        label= 'Phone number: (123)-456-7890',
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': '(xxx)-xxx-xxxx'})
        )
    address = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Address'})
        )
    address_line_2 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Apt, suite, etc, (optional)'})
        )
    province = forms.ChoiceField(
        required=False,
        choices=PROVINCES,
        widget=forms.Select(attrs={
            'class': 'select-input'})
        )
    city = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'City'})
        )
    postal_code = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Postal Code'})
        )
    is_dealer = forms.BooleanField(
        initial=True,
        required=False,
        widget=forms.CheckboxInput(attrs={'id': 'user-type'}),
        label='Is Dealer',
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_dealer'].disabled = True

    class Meta:
        model = User
        fields = ['email', 'dealer_name', 'password1', 'password2', 'phone_number', 'address', 'address_line_2', 'province', 'city', 'postal_code', 'is_dealer']

"""
class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'placeholder': 'Create a username'
        })
        self.fields["email"].widget.attrs.update({
            'placeholder': 'Enter your email',
        })
        self.fields["first_name"].widget.attrs.update({
            'placeholder': "What's the name of your dealership?"
        })
        self.fields["password1"].widget.attrs.update({
            'placeholder': 'Create a password'
        })
        self.fields["password2"].widget.attrs.update({
            'placeholder': 'Verify your password'
        })

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        labels = {
            'first_name': ('Dealership'),
        }
"""

class CustomerVehicleInfoTwo(ModelForm):
    enable_form = forms.BooleanField(
        required=False,
        label='Vehicle Trade-in?',
        initial=False,
        widget=forms.CheckboxInput(attrs={'onchange': 'enableFields()', 'id': 'id_enable_form'})
    )
    tradeInVin = forms.CharField(
        required=False, label='Trade-in Vin', 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        )
    tradeInPrice = forms.CharField(
        required=False, label='Trade-in Price',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    tradeInMileage = forms.CharField(
        required=False, label='Trade-in Mileage',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    tradeInMake = forms.CharField(
        required=False, label='Trade-in Make',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    tradeInModel = forms.CharField(
        required=False, label='Trade-in Model',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    tradeInTrim = forms.CharField(
        required=False, label='Trade-in Trim',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    tradeInYear = forms.CharField(
        required=False, label='Trade-in Year',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    tradeInColor = forms.CharField(
        required=False, label='Trade-in Color',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    
    class Meta:
        model = CustomerVehicle
        fields = ['enable_form', 'tradeInVin', 'tradeInPrice', 'tradeInMileage', 'tradeInMake', 'tradeInModel', 'tradeInTrim', 'tradeInYear', 'tradeInColor']

class CustomerVehicleInfoThree(ModelForm):
    vehicleFront = forms.FileField(
        required=False,
        label= "Vehicle Front",
        widget=AdminResubmitFileWidget(attrs={'class': 'employment-form-file', 'id': 'vehicle_front'})
    )
    vehicleSide = forms.FileField(
        required=False,
        label= "Vehicle Side",
        widget=AdminResubmitFileWidget(attrs={'class': 'employment-form-file', 'id': 'vehicle_side'})
    )
    vehicleBack = forms.FileField(
        required=False,
        label= "Vehicle Back",
        widget=AdminResubmitFileWidget(attrs={'class': 'employment-form-file', 'id': 'vehicle_back'})
    )
    vehicleOdometer = forms.FileField(
        required=False,
        label= "Vehicle Odometer",
        widget=AdminResubmitFileWidget(attrs={'class': 'employment-form-file', 'id': 'vehicle_odometer'})
    )
    vehicleInterior = forms.FileField(
        required=False,
        label= "Vehicle Interior",
        widget=AdminResubmitFileWidget(attrs={'class': 'employment-form-file', 'id': 'vehicle_interior'})
    )
    exampleDocument1 = forms.FileField(
        required=False,
        label= "Example Document 1",
        widget=AdminResubmitFileWidget(attrs={'class': 'employment-form-file', 'id': 'example_document1'})
    )
    exampleDocument2 = forms.FileField(
        required=False,
        label= "Example Document 3",
        widget=AdminResubmitFileWidget(attrs={'class': 'employment-form-file', 'id': 'example_document2'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = CustomerVehicle
        fields = ['vehicleFront', 'vehicleSide', 'vehicleBack', 'vehicleOdometer', 'vehicleInterior', 'exampleDocument1', 'exampleDocument2']

class VehicleInformationForm(ModelForm):
    vinNumber = forms.CharField(required=False, label='VIN Number')
    stockNumber = forms.CharField(required=False, label='Stock Number')
    vehiclePrice = forms.CharField(required=False, label='Vehicle Price')
    downPayment = forms.CharField(required=False, label='Down Payment')
    vehicleMileage = forms.CharField(required=False, label='Vehicle Mileage')
    make = forms.CharField(required=False, label='Make')
    model = forms.CharField(required=False, label='Model')
    trim = forms.CharField(required=False, label='Trim')
    year = forms.CharField(required=False, label='Year')
    color = forms.CharField(required=False, label='Color')
    status = forms.ChoiceField(
        choices=STATUSCHOICES,
        required=False,
        label='Status',
        widget=forms.Select(attrs={'class': 'customer-form-field-widget'})
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["vinNumber"].widget.attrs.update({
            'placeholder' : 'Enter vin number'
        })
        self.fields["stockNumber"].widget.attrs.update({
            'placeholder' : 'Enter stock number'
        })
        self.fields["vehiclePrice"].widget.attrs.update({
            'placeholder' : 'Enter vehicle price'
        })
        self.fields["downPayment"].widget.attrs.update({
            'placeholder' : 'Down payment'
        })
        self.fields["vehicleMileage"].widget.attrs.update({
            'placeholder' : 'Enter vehicle mileage (KM)'
        })
        self.fields["make"].widget.attrs.update({
            'placeholder' : 'Vehicle make'
        })
        self.fields["model"].widget.attrs.update({
            'placeholder' : 'Vehicle model'
        })
        self.fields["trim"].widget.attrs.update({
            'placeholder' : 'Vehicle trim'
        })
        self.fields["year"].widget.attrs.update({
            'placeholder' : 'Vehicle year'
        })
        self.fields["color"].widget.attrs.update({
            'placeholder' : 'Vehicle color'
        })
    class Meta:
        model = VehicleInformation
        widgets = {
            'vinNumber': forms.TextInput(attrs={'class': 'newform-input'}),
            'stockNumber': forms.TextInput(attrs={'class': 'newform-input'}),
            'vehiclePrice': forms.TextInput(attrs={'class': 'newform-input dollar'}),
            'downPayment': forms.TextInput(attrs={'class': 'newform-input dollar'}),
            'vehicleMileage': forms.TextInput(attrs={'class': 'newform-input'}),
            'make': forms.TextInput(attrs={'class': 'newform-input'}),
            'model': forms.TextInput(attrs={'class': 'newform-input'}),
            'trim': forms.TextInput(attrs={'class': 'newform-input'}),
            'year': forms.TextInput(attrs={'class': 'newform-input'}),
            'color': forms.TextInput(attrs={'class': 'newform-input'}),
        }
        fields = ['vinNumber', 'stockNumber', 'vehiclePrice', 'downPayment', 'vehicleMileage', 'make', 'model', 'trim', 'year', 'color']
        labels = {
            'vinNumber' : ('VIN Number'),
            'stockNumber' : ('Stock Number'),
            'vehiclePrice' : ('Vehicle Price'),
            'downPayment' : ('Down Payment'),
            'vehicleMileage' : ('Vehicle Kilometers'),
            'make' : ('Make'),
            'model' : ('Model'),
            'trim' : ('Trim'),
            'year' : ('Year'),
            'color' : ('Color'),
            'status' : ('Status'),
            'dealership': ('DealerShip'),
        }

class TradeInInformationForm(ModelForm):
    enable_form = forms.BooleanField(
        required=False,
        label='Vehicle Trade-in?',
        initial=False,
        widget=forms.CheckboxInput(attrs={'onchange': 'enableFields()', 'id': 'id_enable_form'})
    )
    tradeInVin = forms.CharField(required=False, label='Trade-in Vin', 
                                 widget=forms.TextInput(attrs={'class': 'form-control'})
                                 )
    tradeInPrice = forms.CharField(required=False, label='Trade-in Price',
                                   widget=forms.TextInput(attrs={'class': 'form-control'})
                                   )
    tradeInMileage = forms.CharField(required=False, label='Trade-in Mileage',
                                     widget=forms.TextInput(attrs={'class': 'form-control'})
                                     )
    tradeInMake = forms.CharField(required=False, label='Trade-in Make',
                                  widget=forms.TextInput(attrs={'class': 'form-control'})
                                  )
    tradeInModel = forms.CharField(required=False, label='Trade-in Model',
                                   widget=forms.TextInput(attrs={'class': 'form-control'})
                                   )
    tradeInTrim = forms.CharField(required=False, label='Trade-in Trim',
                                  widget=forms.TextInput(attrs={'class': 'form-control'})
                                  )
    tradeInYear = forms.CharField(required=False, label='Trade-in Year',
                                  widget=forms.TextInput(attrs={'class': 'form-control'})
                                  )
    tradeInColor = forms.CharField(required=False, label='Trade-in Color',
                                   widget=forms.TextInput(attrs={'class': 'form-control'})
                                   )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tradeInVin"].widget.attrs.update({
            'placeholder' : 'VIN number'
        })
        self.fields["tradeInPrice"].widget.attrs.update({
            'placeholder' : 'Vehicle price'
        })
        self.fields["tradeInMileage"].widget.attrs.update({
            'placeholder' : 'Vehicle mileage (KM)'
        })
        self.fields["tradeInMake"].widget.attrs.update({
            'placeholder' : 'Vehicle make'
        })
        self.fields["tradeInModel"].widget.attrs.update({
            'placeholder' : 'Vehicle model'
        })
        self.fields["tradeInTrim"].widget.attrs.update({
            'placeholder' : 'Vehicle trim'
        })
        self.fields["tradeInYear"].widget.attrs.update({
            'placeholder' : 'Vehicle year'
        })
        self.fields["tradeInColor"].widget.attrs.update({
            'placeholder' : 'Vehicle Color'
        })
    class Meta:
        model = VehicleInformation
        widgets = {
            'tradeInVin': forms.TextInput(attrs={'class': 'form-control', 'disabled': True}),
            'tradeInPrice': forms.TextInput(attrs={'class': 'form-control', 'disabled': True}),
            'tradeInMileage': forms.TextInput(attrs={'class': 'form-control', 'disabled': True}),
            'tradeInMake': forms.TextInput(attrs={'class': 'form-control', 'disabled': True}),
            'tradeInModel': forms.TextInput(attrs={'class': 'form-control', 'disabled': True}),
            'tradeInTrim': forms.TextInput(attrs={'class': 'form-control', 'disabled': True}),
            'tradeInYear': forms.TextInput(attrs={'class': 'form-control', 'disabled': True}),
            'tradeInColor': forms.TextInput(attrs={'class': 'form-control', 'disabled': True}),
        }
        fields = ['enable_form', 'tradeInVin', 'tradeInPrice', 'tradeInMileage', 'tradeInMake', 'tradeInModel', 'tradeInTrim', 'tradeInYear', 'tradeInColor']
        labels = {
            'tradeInVin' : ('Trade-in VIN'),
            'tradeInPrice' : ('Trade-in Price'),
            'tradeInMileage' : ('Trade-in Kilometers'),
            'tradeInMake' : ('Trade-in Make'),
            'tradeInModel' : ('Trade-in Model'),
            'tradeInTrim' : ('Trade-in Trim'),
            'tradeInYear' : ('Trade-in Year'),
            'tradeInColor' : ('Trade-in Color'),
        }

class EmploymentInformationForm(ModelForm):
    employment_status = forms.ChoiceField(
        required=False,
        label= 'Employment status',
        choices=EMPLOYMENT,
        widget=forms.Select(attrs={'class': 'customer-form-field-widget'})
    )
    company_name = forms.CharField(
        required=False,
        label= 'Company name',
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Company Name'})
    )
    job_title = forms.CharField(
        required=False,
        label= 'Job title',
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Job Title'})
    )
    employment_length = forms.CharField(
        required=False,
        label= 'Employment length',
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Employment Length'})
    )
    salary = forms.CharField(
        required=False,
        label = 'Salary',
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Salary'})
    )
    monthly_income = forms.CharField(
        required=False,
        label= 'Monthly income',
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Monthly Income'})
    )
    other_income = forms.CharField(
        required=False,
        label= 'Other income',
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Other Income'})
    )
    paystub_file = forms.FileField(
        required=False,
        label= 'Paystub file',
        widget=AdminResubmitFileWidget(attrs={'class': 'employment-form-file'})
    )
    tax_return = forms.FileField(
        required=False,
        label= 'Tax return',
        widget=AdminResubmitFileWidget(attrs={'class': 'employment-form-file tax-return'})
    )
    
    class Meta:
        model = VehicleInformation
        fields = ['employment_status', 'company_name', 'job_title', 'employment_length', 'salary', 'monthly_income', 'other_income', 'paystub_file', 'tax_return']
        labels = {
            'employment_status': 'Employment Status',
            'company_name': 'Company Name',
            'job_title': 'Job Title',
            'employment_length': 'Employment Length',
            'salary': 'Salary',
            'monthly_income': 'Monthly Income',
            'other_income': 'Other Income',
            'paystub_file': 'Pay stub',
            'tax_return': 'Tax Return',
        }


class PersonalInformationForm(ModelForm):
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'First Name'})
        )
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Last Name'})
    )
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'customer-form-field',
            'type': 'date'
        }))
    phone_number = PhoneNumberField(
        required=False,
        label= 'Phone number: (123)-456-7890',
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': '(xxx)-xxx-xxxx'})
        )
    email = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'example@example.com'})
        )
    address = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Address'})
        )
    address_line_2 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Apt, suite, etc, (optional)'})
        )
    province = forms.ChoiceField(
        required=False,
        choices=PROVINCES,
        widget=forms.Select(attrs={
            'class': 'customer-form-field-widget',
            'label': 'asdasdadadada',
        })
    )
    city = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'City'})
        )
    postal_code = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'Postal Code'})
        )
    social_insurance_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'placeholder': 'SIN Number'})
        )
    drivers_license = forms.FileField(
        required=False,
        widget=AdminResubmitFileWidget(attrs={'class': 'employment-form-file', 'id': 'drivers_license'})
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = VehicleInformation
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'customer-form-field', 'required': 'False'}),
            'last_name': forms.TextInput(attrs={'class': 'customer-form-field', 'required': 'False'}),
            'phone_number': forms.TextInput(attrs={'class': 'customer-form-field', 'required': 'False'}),
            'email': forms.TextInput(attrs={'class': 'customer-form-field', 'required': 'False'}),
            'address': forms.TextInput(attrs={'class': 'customer-form-field', 'required': 'False'}),
            'address_line_2': forms.TextInput(attrs={'class': 'customer-form-field', 'required': 'False'}),
            'province': forms.Select(attrs={'class': 'customer-form-field-widget', 'required': 'False'}),
            'city': forms.TextInput(attrs={'class': 'customer-form-field', 'required': 'False'}),
            'postal_code': forms.TextInput(attrs={'class': 'customer-form-field', 'required': 'False'}),
            'social_insurance_number': forms.TextInput(attrs={'class': 'customer-form-field', 'required': 'False'}),
        }
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'email', 'address', 'address_line_2', 'province', 'city', 'postal_code', 'social_insurance_number', 'drivers_license']
        labels = {
            'first_name': ('First Name'),
            'last_name': ('Last Name'),
            'date_of_birth': ('Date of Birth'),
            'phone_number': ('Phone Number (xxx)-xxx-xxxx'),
            'email': ('Email'),
            'address': ('Address'),
            'address_line_2': ('Address Line 2'),
            'city': ('City'),
            'postal_code': ('Postal Code'),
            'social_insurance_number': ('Social Insurance #'),
            'drivers_license': ('Drivers License'),
        }

class DocumentationForm(ModelForm):
    vehicleFront = forms.FileField(
        required=False,
        widget=AdminResubmitFileWidget(attrs={'class': 'employment-form-file', 'id': 'vehicle_front'})
    )
    vehicleSide = forms.FileField(
        required=False,
        widget=AdminResubmitFileWidget(attrs={'class': 'employment-form-file', 'id': 'vehicle_side'})
    )
    vehicleBack = forms.FileField(
        required=False,
        widget=AdminResubmitFileWidget(attrs={'class': 'employment-form-file', 'id': 'vehicle_back'})
    )
    vehicleOdometer = forms.FileField(
        required=False,
        widget=AdminResubmitFileWidget(attrs={'class': 'employment-form-file', 'id': 'vehicle_odometer'})
    )
    vehicleInterior = forms.FileField(
        required=False,
        widget=AdminResubmitFileWidget(attrs={'class': 'employment-form-file', 'id': 'vehicle_interior'})
    )
    exampleDocument1 = forms.FileField(
        required=False,
        widget=AdminResubmitFileWidget(attrs={'class': 'employment-form-file', 'id': 'example_document1'})
    )
    exampleDocument2 = forms.FileField(
        required=False,
        widget=AdminResubmitFileWidget(attrs={'class': 'employment-form-file', 'id': 'example_document2'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = VehicleInformation
        fields = ['vehicleFront', 'vehicleSide', 'vehicleBack', 'vehicleOdometer', 'vehicleInterior', 'exampleDocument1', 'exampleDocument2']
        labels = {
            'vehicle_front': 'Vehicle Front',
            'vehicle_side': 'Vehicle Side',
            'vehicle_back': 'Vehicle Back',
            'vehicle_odometer': 'Vehicle Odometer',
            'vehicle_interior': 'Vehicle Interior',
            'example_document1': 'Example Document 1',
            'example_document2': 'Example Document 2',
        }


#class CustomerForm(forms.ModelForm):
    #class Meta:
        #model = Customer
        #fields = ['first_name', 'last_name', 'email', 'phone_number']


#class DealerFinanceForm(forms.ModelForm):
    #class Meta:
        #model = VehicleInformation
        #fields = ['vinNumber', 'stockNumber', 'vehiclePrice', 'downPayment', 'tradeInPrice',
                  #'vehicleMileage', 'make', 'model', 'trim', 'year', 'color', 'fuelType']

        #labels = {
            #'vinNumber': ('VIN Number'),
            #'stockNumber': ('Stock Number'),
            #'vehiclePrice': ('Vehicle Price'),
            #'tradeInPrice': ('Trade In Price'),
            #'downPayment': ('Down Payment'),
            #'vehicleMileage': ('Vehicle Mileage (KM)'),
            #'make': ('Vehicle Make'),
            #'model': ('Vehicle Model'),
            #'trim': ('Vehicle Trim'),
            #'year': ('Vehicle Year'),
            #'color': ('Vehicle Color'),
            #'fuelType': ('Vehicle Fuel Type'),
            #'dealership': ('Dealership'),
        #}


#class EmploymentInformationForm(forms.ModelForm):
    #class Meta:
        #model = EmploymentInformation
        #fields = ['company_name', 'job_title', 'salary']
        #labels = {'company_name': ('Company Name'),
                    #'job_title': ('Job Title'),
                    #'salary': ('Salary')}


#class DealerFinanceForm(forms.Form):
    #customer_form = CustomerForm()
    #vehicle_form = VehicleInformationForm()
    #employment_form = EmploymentInformationForm()

# class DealerFinanceForm(ModelForm):
    # vinNumber = forms.TextInput()
    # stockNumber = forms.TextInput()
    # vehiclePrice = forms.TextInput()
    # downPayment = forms.TextInput()
    # tradeInPrice = forms.TextInput()
    # vehicleMileage = forms.TextInput()
    # make = forms.TextInput()
    # model = forms.TextInput()
    # trim = forms.TextInput()
    # year = forms.TextInput()
    # color = forms.TextInput()
    # fuelType = forms.TextInput()
    # status = forms.TextInput()

    # def __init__(self, request, *args, **kwargs):
    # super().__init__(*args, **kwargs)
    # placeholders = {
    # 'vinNumber': 'Enter vin number',
    # 'stockNumber': 'Enter stock number',
    # 'vehiclePrice': 'Enter vehicle price',
    # 'downPayment': 'Down payment',
    # 'tradeInPrice': 'Trade in price',
    # 'vehicleMileage': 'Enter vehicle mileage (KM)',
    # 'make': 'Vehicle make',
    # 'model': 'Vehicle model',
    # 'trim': 'Vehicle trim',
    # 'year': 'Vehicle year',
    # 'color': 'Vehicle color',
    # 'fuelType': 'Vehicle fuel type',
    # }
    # for field in self.fields:
    # self.fields[field].widget.attrs.update(
    # {'placeholder': placeholders[field]})

    # class Meta:
    # model = VehicleInformation
    # widgets = {
    # 'vinNumber': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'stockNumber': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'vehiclePrice': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'tradeInPrice': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'downPayment': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'vehicleMileage': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'make': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'model': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'trim': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'year': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'color': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'fuelType': forms.TextInput(attrs={'class': 'newform-input'}),
    # }
    # fields = ['vinNumber', 'stockNumber', 'vehiclePrice', 'tradeInPrice', 'downPayment',
    # 'vehicleMileage', 'make', 'model', 'trim', 'year', 'color', 'fuelType']  # , 'dealership']
    # labels = {
    # 'vinNumber': ('VIN Number'),
    # 'stockNumber': ('Stock Number'),
    # 'vehiclePrice': ('Vehicle Price'),
    # 'tradeInPrice': ('Trade In Price'),
    # 'downPayment': ('Down Payment'),
    # 'vehicleMileage': ('Vehicle Mileage (KM)'),
    # 'make': ('Vehicle Make'),
    # 'model': ('Vehicle Model'),
    # 'trim': ('Vehicle Trim'),
    # 'year': ('Vehicle Year'),
    # 'color': ('Vehicle Color'),
    # 'fuelType': ('Vehicle Fuel Type'),
    # 'dealership' : ('Dealership'),
    # }


# class DealerFinanceForm(ModelForm):
    # vinNumber = forms.TextInput()
    # stockNumber = forms.TextInput()
    # vehiclePrice = forms.TextInput()
    # downPayment = forms.TextInput()
    # tradeInPrice = forms.TextInput()
    # vehicleMileage = forms.TextInput()
    # make = forms.TextInput()
    # model = forms.TextInput()
    # trim = forms.TextInput()
    # year = forms.TextInput()
    # color = forms.TextInput()
    # fuelType = forms.TextInput()
    # status = forms.TextInput()

    # def __init__(self, request, *args, **kwargs):
    # super().__init__(*args, **kwargs)
    # self.fields["vinNumber"].widget.attrs.update({
    # 'placeholder' : 'Enter vin number'
    # })
    # self.fields["stockNumber"].widget.attrs.update({
    # 'placeholder' : 'Enter stock number'
    # })
    # self.fields["vehiclePrice"].widget.attrs.update({
    # 'placeholder' : 'Enter vehicle price'
    # })
    # self.fields["downPayment"].widget.attrs.update({
    # 'placeholder' : 'Down payment'
    # })
    # self.fields["tradeInPrice"].widget.attrs.update({
    # 'placeholder' : 'Trade in price'
    # })
    # self.fields["vehicleMileage"].widget.attrs.update({
    # 'placeholder' : 'Enter vehicle mileage (KM)'
    # })
    # self.fields["make"].widget.attrs.update({
    # 'placeholder' : 'Vehicle make'
    # })
    # self.fields["model"].widget.attrs.update({
    # 'placeholder' : 'Vehicle model'
    # })
    # self.fields["trim"].widget.attrs.update({
    # 'placeholder' : 'Vehicle trim'
    # })
    # self.fields["year"].widget.attrs.update({
    # 'placeholder' : 'Vehicle year'
    # })
    # self.fields["color"].widget.attrs.update({
    # 'placeholder' : 'Vehicle color'
    # })
    # self.fields["fuelType"].widget.attrs.update({
    # 'placeholder' : 'Vehicle fuel type'
    # })
    # self.fields['dealership'].initial = request.user.dealership

    # class Meta:
    # model = VehicleInformation
    # widgets = {
    # 'vinNumber': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'stockNumber': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'vehiclePrice': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'tradeInPrice': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'downPayment': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'vehicleMileage': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'make': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'model': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'trim': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'year': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'color': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'fuelType': forms.TextInput(attrs={'class': 'newform-input'}),
    # 'dealership': forms.TextInput(attrs={'class': 'newform-input'}),
    # }
    # fields = ['vinNumber', 'stockNumber', 'vehiclePrice', 'tradeInPrice', 'downPayment', 'vehicleMileage', 'make', 'model', 'trim', 'year', 'color', 'fuelType']#, 'dealership']
    # labels = {
    # 'vinNumber' : ('VIN Number'),
    # 'stockNumber' : ('Stock Number'),
    # 'vehiclePrice' : ('Vehicle Price'),
    # 'tradeInPrice' : ('Trade In Price'),
    # 'downPayment' : ('Down Payment'),
    # 'vehicleMileage' : ('Vehicle Kilometers'),
    # 'make' : ('Make'),
    # 'model' : ('Model'),
    # 'trim' : ('Trim'),
    # 'year' : ('Year'),
    # 'color' : ('Color'),
    # 'fuelType' : ('Fuel Type'),
    # }
