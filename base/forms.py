from .models import VehicleInformation 
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from .models import VehicleInformation


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
            'vehiclePrice': forms.TextInput(attrs={'class': 'newform-input'}),
            'tradeInPrice': forms.TextInput(attrs={'class': 'newform-input'}),
            'downPayment': forms.TextInput(attrs={'class': 'newform-input'}),
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
