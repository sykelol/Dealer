from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import default_storage
from .forms import VehicleInformationForm, CreateUserForm, EmploymentInformationForm, PersonalInformationForm, TradeInInformationForm, DocumentationForm
from .models import VehicleInformation, CustomerInformation
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import DefaultStorage
from django.core.files.base import ContentFile
from django.conf import settings
import tempfile
import os
from django.core.files.storage import FileSystemStorage
from django.views.decorators.http import require_POST
import uuid
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import boto3
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

def broker_required(view_func):
    def check_user_is_broker(user):
        return user.is_authenticated and user.is_staff
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

def financingform(request):
    return render(request, 'landingpage.html')

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

@login_required
def newform(request):
    if request.method == 'POST':
        form = VehicleInformationForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if hasattr(request.user, 'dealership'):
                form.dealership = request.user.dealership
            else:
                # Set a default value for the dealership
                form.dealership = 'Unknown'
            form.save()
            return redirect('mydeals')
    else:
        form = VehicleInformationForm()
    return render(request, 'newform.html', {'form': form})


@login_required
def mydeals(request):
    if hasattr(request.user, 'dealership'):
        # User is a dealership
        dealership = request.user.dealership
        deals = VehicleInformation.objects.filter(
            Q(dealership=dealership, status='approved') | Q(status='declined'))
    else:
        # User is a broker
        deals = VehicleInformation.objects.filter(Q(status='approved') | Q(status='declined'))
        # deals = VehicleInformation.objects.all()
    return render(request, 'mydeals.html', {'deals': deals})


@login_required
def pendingdeals(request):
    if hasattr(request.user, 'dealership'):
        # User is a dealership
        dealership = request.user.dealership
        deals = VehicleInformation.objects.filter(
            dealership=dealership, status='pending')
    else:
        # User is a broker
        deals = VehicleInformation.objects.filter(status='pending')
    return render(request, 'pendingdeals.html', {'deals': deals})


@broker_required
def updateform(request, id):
    update = VehicleInformation.objects.get(id=id)
    form = VehicleInformationForm(instance=update)
    if request.method == 'POST':
        form = VehicleInformationForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('mydeals')
    context = {'form': form}
    return render(request, 'newform.html', context)


@broker_required
def dealernewform(request):
    form = VehicleInformationForm()
    if request.method == 'POST':
        form = VehicleInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mydeals')
    return render(request, 'dealernewform.html', {'form': form})

@broker_required
def updatestatus(request, id):
    update = VehicleInformation.objects.get(id=id)
    form = VehicleInformationForm(instance=update)
    if request.method == 'POST':
        form = VehicleInformationForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('mydeals')
    context = {'form': form}
    return render(request, 'updatestatus.html', context)


class NewFormWizard(SessionWizardView):
    template_name = "newform.html"
    form_list = [PersonalInformationForm, EmploymentInformationForm, VehicleInformationForm, TradeInInformationForm, DocumentationForm]
    file_storage = default_storage

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        personal_data = form_data[0]
        employment_data = form_data[1]
        vehicle_data = form_data[2]
        tradein_data = form_data[3]
        documentation_data = form_data[4]
        vehicle_info_data = {
            'first_name': personal_data['first_name'],
            'last_name': personal_data['last_name'],
            'date_of_birth': personal_data['date_of_birth'],
            'phone_number': personal_data['phone_number'],
            'email': personal_data['email'],
            'address': personal_data['address'],
            'address_line_2': personal_data['address_line_2'],
            'province': personal_data['province'],
            'city': personal_data['city'],
            'postal_code': personal_data['postal_code'],
            'social_insurance_number': personal_data['social_insurance_number'],
            'employment_status': employment_data['employment_status'],
            'company_name': employment_data['company_name'],
            'job_title': employment_data['job_title'],
            'employment_length': employment_data['employment_length'],
            'salary': employment_data['salary'],
            'monthly_income': employment_data['monthly_income'],
            'other_income': employment_data['other_income'],
            'paystub_file': employment_data['paystub_file'],
            'tax_return': employment_data['tax_return'],
            'vinNumber': vehicle_data['vinNumber'],
            'stockNumber': vehicle_data['stockNumber'],
            'vehiclePrice': vehicle_data['vehiclePrice'],
            'downPayment': vehicle_data['downPayment'],
            'vehicleMileage': vehicle_data['vehicleMileage'],
            'make': vehicle_data['make'],
            'model': vehicle_data['model'],
            'trim': vehicle_data['trim'],
            'year': vehicle_data['year'],
            'color': vehicle_data['color'],
            'tradeInVin': tradein_data['tradeInVin'],
            'tradeInPrice': tradein_data['tradeInPrice'],
            'tradeInMileage': tradein_data['tradeInMileage'],
            'tradeInMake': tradein_data['tradeInMake'],
            'tradeInModel': tradein_data['tradeInModel'],
            'tradeInTrim': tradein_data['tradeInTrim'],
            'tradeInYear': tradein_data['tradeInYear'],
            'tradeInColor': tradein_data['tradeInColor'],
            'vehicle_front': documentation_data['vehicle_front'],
            'vehicle_side': documentation_data['vehicle_side'],
            'vehicle_back': documentation_data['vehicle_back'],
            'vehicle_odometer': documentation_data['vehicle_odometer'],
            'vehicle_interior': documentation_data['vehicle_interior'],
            'example_document1': documentation_data['example_document1'],
            'example_document2': documentation_data['example_document2'],
        }
        form = VehicleInformation(**vehicle_info_data)
        form.save()
        return render(self.request, 'pendingdeals.html')

"""
def PersonalInformationView(request):
    if request.method == 'POST':
        form = PersonalInformationForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle file uploads
            myfile = request.FILES['drivers_license']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            # Save form data to session
            request.session['form_data'].update({'PersonalInformationForm': form.cleaned_data})
            request.session['form_data'].update({'drivers_license': uploaded_file_url})
            return redirect('employmentinformationview')
    else:
        form = PersonalInformationForm()
    return render(request, 'personalinformationform.html', {'form': form})

"""


class CustomerFinancingWizard(SessionWizardView):
    template_name = "customerfinancingform.html"
    form_list = [PersonalInformationForm, EmploymentInformationForm]
    file_storage = DefaultStorage()

    def get_form(self, step=None, data=None, files=None):
        form = super().get_form(step, data, files)
        file_data = cache.get('file_data')
        if file_data:
            if step == '1':
                PersonalInformationForm.fields['drivers_license'].initial = file_data.get('drivers_license')
            if step == '2':
                form.fields['paystub_file'].initial = file_data.get('paystub_file')
                form.fields['tax_return'].initial = file_data.get('tax_return')
        return form
    
    def process_step(self, form):
        if self.request.method == 'POST':
            if not form.is_valid():
                file_data = cache.get('file_data') or {}
                file_data.update(self.request.FILES)
                cache.set('file_data', file_data, timeout=60*60)
                return self.render(self.get_template_names(), self.get_context_data(form=form))
        return super().process_step(form)

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        personal_data = form_data[0]
        employment_data = form_data[1]
        customer_info_data = {
            'first_name': personal_data['first_name'],
            'last_name': personal_data['last_name'],
            'date_of_birth': personal_data['date_of_birth'],
            'phone_number': personal_data['phone_number'],
            'email': personal_data['email'],
            'address': personal_data['address'],
            'address_line_2': personal_data['address_line_2'],
            'province': personal_data['province'],
            'city': personal_data['city'],
            'postal_code': personal_data['postal_code'],
            'social_insurance_number': personal_data['social_insurance_number'],
            'drivers_license': personal_data['drivers_license'],
            'employment_status': employment_data['employment_status'],
            'company_name': employment_data['company_name'],
            'job_title': employment_data['job_title'],
            'employment_length': employment_data['employment_length'],
            'salary': employment_data['salary'],
            'monthly_income': employment_data['monthly_income'],
            'other_income': employment_data['other_income'],
            'paystub_file': employment_data['paystub_file'],
            'tax_return': employment_data['tax_return'],
        }
        file_data = cache.get('file_data')
        if file_data:
            file_data = cache.get('file_data')
            customer_info_data['drivers_license'] = file_data.get('drivers_license')
            customer_info_data['paystub_file'] = file_data.get('paystub_file')
            customer_info_data['tax_return'] = file_data.get('tax_return')
            print(file_data.get('drivers_license'))
        customer = CustomerInformation.objects.create(**customer_info_data)
        return render(self.request, 'successmessage.html', {'form_data': form_data, 'customer': customer})

'''
def personalInformationView(request):
    if request.method == 'POST':
        form = PersonalInformationForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES.get('drivers_license')
            if uploaded_file:
                s3 = boto3.client('s3')
                file_path = uploaded_file.path
                file_name = uploaded_file.name
                s3.upload_file(file_path, 'virtualcargeeks-bucket', file_name)
                request.session['drivers_license'] = file_name
            
            instance = form.save()
            return redirect('employmentinformationview', instance_id=instance.id)
    else:
        form = PersonalInformationForm()

    uploaded_file = None
    file_name = request.session.get('drivers_license')
    if file_name:
        # Retrieve the uploaded file from Amazon S3
        s3 = boto3.client('s3')
        file = BytesIO()
        s3.download_fileobj('virtualcargeeks-bucket', file_name, file)
        uploaded_file = InMemoryUploadedFile(file, None, file_name, 'application/octet-stream', file.getbuffer().nbytes, None)
        form.initial['drivers_license'] = uploaded_file
        
    return render(request, 'personalinformationform.html', {'form': form, 'uploaded_file': uploaded_file})
'''

'''
def employmentInformationView(request, instance_id):
    instance = CustomerInformation.objects.get(id=instance_id)
    if request.method == 'POST':
        form = StatusInformationForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('successmessage')
    else:
        form = StatusInformationForm(instance=instance)
    return render(request, 'employmentinformationform.html', {'form': form})
'''

def updateform(request, id):
    update = VehicleInformation.objects.get(id=id)
    form = VehicleInformationForm(instance=update)
    if request.method == 'POST':
        form = VehicleInformationForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('mydeals')
    context = {'form': form}
    return render(request, 'newform.html', context)

class CustomerFinancingWizard(SessionWizardView):
    template_name = "customerfinancingform.html"
    form_list = [PersonalInformationForm, EmploymentInformationForm]
    file_storage = DefaultStorage()

    def form_valid(self, form):
        if self.step == '0':
            # Step 0 is the PersonalInformationForm
            driver_license = self.request.FILES.get('drivers_license', None)
            if driver_license:
                driver_license_path = self.file_storage.save(driver_license.name, driver_license)
                self.request.session['drivers_license'] = driver_license_path
        return super().form_valid(form)


'''
class CustomerFinancingWizard(SessionWizardView):
    template_name = "customerfinancingform.html"
    form_list = [PersonalInformationForm, EmploymentInformationForm]
    file_storage = DefaultStorage()

    def form_valid(self, form):
        if self.step == '0':
            # Step 0 is the PersonalInformationForm
            driver_license = self.request.FILES.get('drivers_license', None)
            if driver_license:
                driver_license_path = self.file_storage.save(driver_license.name, driver_license)
                self.request.session['drivers_license'] = driver_license_path
        elif self.step == '1':
            # Step 1 is the StatusInformationForm
            paystub_file = self.request.FILES.get('paystub_file', None)
            tax_return = self.request.FILES.get('tax_return', None)
            if paystub_file:
                paystub_file_path = self.file_storage.save(paystub_file.name, paystub_file)
                self.request.session['paystub_file'] = paystub_file_path
            if tax_return:
                tax_return_path = self.file_storage.save(tax_return.name, tax_return)
                self.request.session['tax_return'] = tax_return_path
        return super().form_valid(form)

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        personal_data = form_data[0]
        employment_data = form_data[1]
        customer_info_data = {
            'first_name': personal_data['first_name'],
            'last_name': personal_data['last_name'],
            'date_of_birth': personal_data['date_of_birth'],
            'phone_number': personal_data['phone_number'],
            'email': personal_data['email'],
            'address': personal_data['address'],
            'address_line_2': personal_data['address_line_2'],
            'province': personal_data['province'],
            'city': personal_data['city'],
            'postal_code': personal_data['postal_code'],
            'social_insurance_number': personal_data['social_insurance_number'],
            'drivers_license': self.request.session.get('drivers_license', None),
            'employment_status': employment_data['employment_status'],
            'company_name': employment_data['company_name'],
            'job_title': employment_data['job_title'],
            'employment_length': employment_data['employment_length'],
            'salary': employment_data['salary'],
            'monthly_income': employment_data['monthly_income'],
            'other_income': employment_data['other_income'],
            'paystub_file': self.request.session.get('paystub_file', None),
            'tax_return': self.request.session.get('tax_return', None),
        }
        customer = CustomerInformation.objects.create(**customer_info_data)
        return render(self.request, 'successmessage.html')
'''

def successmessage(request):
    return render(request, 'successmessage.html')

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

