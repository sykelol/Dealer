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
            'placeholder' : 'Create a username'
        })
        self.fields["email"].widget.attrs.update({
            'placeholder' : 'Enter your email',
        })
        self.fields["first_name"].widget.attrs.update({
            'placeholder' : "What's the name of your dealership?"
        })
        self.fields["password1"].widget.attrs.update({
            'placeholder' : 'Create a password'
        })
        self.fields["password2"].widget.attrs.update({
            'placeholder' : 'Verify your password'
        })


    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        labels = {
            'first_name': ('Dealership'),
        }
    
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
        }
        fields = ['vinNumber', 'stockNumber', 'vehiclePrice', 'tradeInPrice', 'downPayment', 'vehicleMileage', 'make', 'model', 'trim', 'year', 'color', 'fuelType']
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
        }