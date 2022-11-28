from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Dealer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
from .forms import CreateUserForm


def register(request):
    form = CreateUserForm()
    username = request.POST.get('username')
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    email = request.POST.get('email')

    if request.method == 'POST':

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists.", extra_tags='username-error')
        if User.objects.filter(first_name=first_name):
            messages.error(request, "Dealership name already exists.", extra_tags='dealername-error')
        if User.objects.filter(email=email):
            messages.error(request, "Email is already in use.", extra_tags='email-error')

        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
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
            return redirect('home')
        else: messages.error(request, '* Username or password does not exist.')

    context = {}
    return render(request, "dealersignin.html", context)


def logoutUser(request):
    logout(request)
    return redirect('home')