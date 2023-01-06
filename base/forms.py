from .models import VehicleInformation 
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from .models import VehicleInformation
from .models import CustomerInformation
from django.forms import DateInput
from phonenumber_field.formfields import PhoneNumberField

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

status_choices = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('declined', 'Declined'),
]

class DealerFinanceForm(ModelForm):
    vinNumber = forms.TextInput()
    stockNumber = forms.TextInput()
    vehiclePrice = forms.TextInput()
    downPayment = forms.TextInput()
    tradeInPrice = forms.TextInput()
    vehicleMileage = forms.TextInput()
    make = forms.TextInput()
    model = forms.TextInput()
    trim = forms.TextInput()
    year = forms.TextInput()
    color = forms.TextInput()
    fuelType = forms.TextInput()
    status = forms.TextInput()
    
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
        self.fields["tradeInPrice"].widget.attrs.update({
            'placeholder' : 'Trade in price'
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
        self.fields["fuelType"].widget.attrs.update({
            'placeholder' : 'Vehicle fuel type'
        })
    class Meta:
        model = VehicleInformation
        widgets = {
            'vinNumber': forms.TextInput(attrs={'class': 'newform-input'}),
            'stockNumber': forms.TextInput(attrs={'class': 'newform-input'}),
            'vehiclePrice': forms.TextInput(attrs={'class': 'newform-input dollar'}),
            'tradeInPrice': forms.TextInput(attrs={'class': 'newform-input dollar'}),
            'downPayment': forms.TextInput(attrs={'class': 'newform-input dollar'}),
            'vehicleMileage': forms.TextInput(attrs={'class': 'newform-input'}),
            'make': forms.TextInput(attrs={'class': 'newform-input'}),
            'model': forms.TextInput(attrs={'class': 'newform-input'}),
            'trim': forms.TextInput(attrs={'class': 'newform-input'}),
            'year': forms.TextInput(attrs={'class': 'newform-input'}),
            'color': forms.TextInput(attrs={'class': 'newform-input'}),
            'fuelType': forms.TextInput(attrs={'class': 'newform-input'}),
            'status': forms.Select(choices=status_choices, attrs={'class': 'newform-input'}),
        }
        fields = ['vinNumber', 'stockNumber', 'vehiclePrice', 'tradeInPrice', 'downPayment', 'vehicleMileage', 'make', 'model', 'trim', 'year', 'color', 'fuelType', 'status']
        labels = {
            'vinNumber' : ('VIN Number'),
            'stockNumber' : ('Stock Number'),
            'vehiclePrice' : ('Vehicle Price'),
            'tradeInPrice' : ('Trade In Price'),
            'downPayment' : ('Down Payment'),
            'vehicleMileage' : ('Vehicle Kilometers'),
            'make' : ('Make'),
            'model' : ('Model'),
            'trim' : ('Trim'),
            'year' : ('Year'),
            'color' : ('Color'),
            'fuelType' : ('Fuel Type'),
            'status' : ('Status'),
        }

EMPLOYMENT = (
    ('employed', 'Employed'),
    ('self-employed', 'Self-employed'),
    ('unemployed', 'Unemployed'),
)

class EmploymentInformationForm(ModelForm):
    employment_status = forms.ChoiceField(
        choices=[
            ('full-time', 'Full-time'),
            ('part-time', 'Part-time'),
            ('temporary', 'Temporary'),
            ('contract', 'Contract'),
            ('self-employed', 'Self-employed'),
            ('retired', 'Retired'),
            ('unemployed', 'Unemployed'),
        ]
    )
    employment_status = forms.ChoiceField(
        choices=EMPLOYMENT,
        widget=forms.Select(attrs={'class': 'customer-form-field-widget'})
    )
    company_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'customer-form-field'})
    )
    job_title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'customer-form-field'})
    )
    employment_length = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'customer-form-field'})
    )
    salary = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'customer-form-field'})
    )
    monthly_income = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'customer-form-field'})
    )
    other_income = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'customer-form-field'})
    )
    paystub_file = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'employment-form-file'})
    )
    tax_return = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'employment-form-file'})
    )
    
    class Meta:
        model = CustomerInformation
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

PROVINCES = (
    ('AB', 'Alberta'),
    ('BC', 'British Columbia'),
    ('MB', 'Manitoba'),
    ('NB', 'New Brunswick'),
    ('NL', 'Newfoundland and Labrador'),
    ('NS', 'Nova Scotia'),
    ('NT', 'Northwest Territories'),
    ('NU', 'Nunavut'),
    ('ON', 'Ontario'),
    ('PE', 'Prince Edward Island'),
    ('QC', 'Quebec'),
    ('SK', 'Saskatchewan'),
    ('YT', 'Yukon'),
)

class PersonalInformationForm(ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'customer-form-field'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'customer-form-field'})
    )
    date_of_birth = forms.DateField(
        widget=DateInput(attrs={'class': 'customer-form-field-widget', 'id': 'date-of-birth', 'type': 'date'})
    )
    phone_number = PhoneNumberField(
        widget=forms.TextInput(attrs={'class': 'customer-form-field', 'type': 'tel'})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'customer-form-field'})
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'customer-form-field'})
    )
    address_line_2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'customer-form-field'})
    )
    province = forms.ChoiceField(
        choices=PROVINCES,
        widget=forms.Select(attrs={'class': 'customer-form-field-widget'})
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'customer-form-field'})
    )
    postal_code = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'customer-form-field'})
    )
    social_insurance_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'customer-form-field'})
    )

    class Meta:
        model = CustomerInformation
        widgets = {

        }
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'email', 'address', 'province', 'city', 'postal_code', 'social_insurance_number']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'date_of_birth': 'Date of Birth',
            'phone_number': 'Phone Number',
            'email': 'Email',
            'address': 'Address',
            'address_line_2': 'Address Line 2',
            'province': 'Province',
            'city': 'City',
            'postal_code': 'Postal Code',
            'social_insurance_number': 'Social Insurance Number (SIN)',
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
