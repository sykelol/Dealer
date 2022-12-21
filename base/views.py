from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import DealerFinanceForm, CreateUserForm
from .models import VehicleInformation


def broker_required(view_func):
    def check_user_is_broker(user):
        return user.is_authenticated and user.is_broker
    return user_passes_test(check_user_is_broker)(view_func)


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists.",
                           extra_tags='username-error')
        # if User.objects.filter(first_name=first_name):
            # messages.error(request, "Dealership name already exists.", extra_tags='dealername-error')
        # if User.objects.filter(email=email):
            # messages.error(request, "Email is already in use.", extra_tags='email-error')
        if (password1 != password2):
            messages.error(request, "Passwords do not match.",
                           extra_tags="password-verification-error")
        if (len(password1) < 8):
            messages.error(request, "Password must contain at least 8 characters.",
                           extra_tags="password-length-error")
        if (password1.isdigit() == True):
            messages.error(request, "Password must contain at least one letter.",
                           extra_tags="password-numeric-error")

        if form.is_valid():
            form.save()
            return redirect('sign-in')
    context = {'form': form}
    return render(request, 'register.html', context)


def home(request):
    return render(request, 'index.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            pass

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('pendingdeals')
            # if user.is_superuser:
            # login(request, user)
            # return redirect('pendingdeals')
            # else:
            # login(request, user)
            # return redirect('dealerpendingdeals')
        else:
            messages.error(request, '* Username or password does not exist.')

    context = {}
    return render(request, "dealersignin.html", context)


def logoutUser(request):
    logout(request)
    return redirect('home')


#@broker_required
def newform(request):
    if request.method == 'POST':
        form = DealerFinanceForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.dealership = request.user.dealership
            form.save()
            return redirect('mydeals')
    else:
        form = DealerFinanceForm()
    return render(request, 'newform.html', {'form': form})


@login_required
def mydeals(request):
    if hasattr(request.user, 'dealership'):
        # User is a dealership
        dealership = request.user.dealership
        deals = VehicleInformation.objects.filter(
            dealership=dealership, status='Completed')
    else:
        # User is a broker
        deals = VehicleInformation.objects.filter(status='completed')
        # deals = VehicleInformation.objects.all()
    return render(request, 'mydeals.html', {'deals': deals})


@login_required
def pendingdeals(request):
    if hasattr(request.user, 'dealership'):
        # User is a dealership
        dealership = request.user.dealership
        deals = VehicleInformation.objects.filter(
            dealership=dealership, status='Pending')
    else:
        # User is a broker
        deals = VehicleInformation.objects.filter(status='Pending')
    return render(request, 'pendingdeals.html', {'deals': deals})


@broker_required
def updateform(request, id):
    update = VehicleInformation.objects.get(id=id)
    form = DealerFinanceForm(instance=update)
    if request.method == 'POST':
        form = DealerFinanceForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('mydeals')
    context = {'form': form}
    return render(request, 'newform.html', context)


@broker_required
def dealernewform(request):
    form = DealerFinanceForm()
    if request.method == 'POST':
        form = DealerFinanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mydeals')
    return render(request, 'dealernewform.html', {'form': form})

# def dealermydeals(request):
    # deals = VehicleInformation.objects.all()
    # context = {
    # 'deals': deals,
    # }
    # return render(request, 'dealermydeals.html', context)


# def dealerpendingdeals(request):
    # deals = VehicleInformation.objects.all()
    # context = {
    # 'deals': deals,
    # }
    # return render(request, 'dealerpendingdeals.html', context)

# def pendingdeals(request):
    # deals = VehicleInformation.objects.all()
    # context = {
    # 'deals': deals,
    # }
    # return render(request, 'pendingdeals.html', context)

# def newform(request):
    # Set the initial value of the dealership field to the user's dealership
    # initial_data = {'dealership': request.user.dealership}
    # form = DealerFinanceForm(request=request, initial=initial_data)
    # if request.method == 'POST':
    # form = DealerFinanceForm(request=request, data=request.POST)
    # if form.is_valid():
    # form.save()
    # return redirect('mydeals')
    # return render(request, 'newform.html', {'form': form})

# def newform(request):
    # form = DealerFinanceForm()
    # if request.method == 'POST':
    # form = DealerFinanceForm(request.POST)
    # if form.is_valid():
    # form.save()
    # return redirect('mydeals')
    # return render(request, 'newform.html', {'form': form})

# @login_required
# def mydeals(request):
    # deals = VehicleInformation.objects.all()
    # return render(request, 'mydeals.html', {'deals': deals})
