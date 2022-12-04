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
    tradeInPrice = forms.TextInput()
    downPayment = forms.TextInput()
    vehicleMileage = forms.TextInput()
    make = forms.TextInput()
    model = forms.TextInput()
    trim = forms.TextInput()
    year = forms.TextInput()
    color = forms.TextInput()
    fuelType = forms.TextInput()
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
            'make' : ('Vehicle Make'),
            'model' : ('Vehicle Model'),
            'trim' : ('Vehicle Trim'),
            'year' : ('Vehicle Year'),
            'color' : ('Vehicle Color'),
            'fuelType' : ('Fuel Type'),
        }