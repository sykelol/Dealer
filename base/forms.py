from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


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

    def clean_dealer(self):
        dealership = self.cleaned_data['first_name']
        if User.objects.filter(first_name=dealership).exists():
            raise ValidationError("Email already exists.")
        return dealership


    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        labels = {
            'first_name': ('Dealership'),
        }