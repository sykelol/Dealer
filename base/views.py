from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Dealer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

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

def register(request):
    return render(request, "register.html")

@login_required(login_required)