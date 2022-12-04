from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import DealerFinanceForm
from .models import VehicleInformation

# Create your views here.
from .forms import CreateUserForm


def register(request):
    form = CreateUserForm()
    username = request.POST.get('username')
    first_name = request.POST.get('first_name')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    if request.method == 'POST':

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists.", extra_tags='username-error')
        #if User.objects.filter(first_name=first_name):
            #messages.error(request, "Dealership name already exists.", extra_tags='dealername-error')
        #if User.objects.filter(email=email):
            #messages.error(request, "Email is already in use.", extra_tags='email-error')
        if (password1 != password2):
            messages.error(request, "Passwords do not match.", extra_tags="password-verification-error")
        if (len(password1) < 8):
            messages.error(request, "Password must contain at least 8 characters.", extra_tags="password-length-error")
        if (password1.isdigit() == True):
            messages.error(request, "Password must contain at least one letter.", extra_tags="password-numeric-error")

        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign-in')
    context = {'form':form}
    return render(request, 'register.html', context)

def home(request):
    return render(request, 'index.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        
        except: pass
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else: messages.error(request, '* Username or password does not exist.')

    context = {}
    return render(request, "dealersignin.html", context)


def logoutUser(request):
    logout(request)
    return redirect('home')

def dashboard(request):
    return render(request, 'dashboard.html')



def newform(request):
    if request.POST:
        form = DealerFinanceForm(request.POST)
        if form.is_valid():
            form.save()    
    return render(request, 'newform.html', { 'form' : DealerFinanceForm })



def mydeals(request):
    deals = VehicleInformation.objects.all()
    context = {
        'deals': deals,
    }
    return render(request, 'mydeals.html', context)