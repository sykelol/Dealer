from django.urls import path
from . import views
from .views import NewFormWizard, CustomerFinancingWizard, UpdateFormWizard, BrokerNewFormWizard, BrokerUpdateFormWizard, DealerUpdateCustomerForm, BrokerUpdateCustomerForm
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name="home"),
    path('financingform/', views.financingform, name="financingform"),
    path('customerfinancing/', CustomerFinancingWizard.as_view(), name="customerfinancingform"),
    path('success/', views.successmessage, name="successmessage"),
    path('sign-in/', views.signin, name="sign-in"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('myfinancing/', views.customer_home, name="myfinancing"),
    path('newform/', NewFormWizard.as_view(), name="newform"),
    path('mydeals/', views.mydeals, name="mydeals"),
    path('pendingdeals/', views.pendingdeals, name="pendingdeals"),
    path('updateform/<int:id>/', UpdateFormWizard.as_view(), name="updateform"),
    path('updatecustomerform/<int:id>/', DealerUpdateCustomerForm.as_view(), name="customerupdateform"),
    path('brokerupdatestatus/<int:id>/', views.brokerupdatestatus, name="brokerupdatestatus"),
    path('brokerupdatecustomerstatus/<int:id>/', views.brokerupdatecustomerstatus, name="brokerupdatecustomerstatus"),
    path('brokerpendingdeals/', views.brokerpendingdeals, name="brokerpendingdeals"),
    path('brokernewform/', BrokerNewFormWizard.as_view(), name="brokernewform"),
    path('brokermydeals/', views.brokermydeals, name="brokermydeals"),
    path('brokerupdateform/<int:id>/', BrokerUpdateFormWizard.as_view(), name="brokerupdateform"),
    path('brokerupdatecustomerform/<int:id>/', BrokerUpdateCustomerForm.as_view(), name="brokerupdatecustomerform"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)