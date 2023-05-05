from django.urls import path
from . import views
from .views import NewFormWizard, CustomerFinancingWizard, UpdateFormWizard, BrokerNewFormWizard, BrokerUpdateFormWizard, DealerUpdateCustomerForm, BrokerUpdateCustomerForm, DealerFinancingForm
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

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
    path('brokerviewcustomerdeal/<int:id>/', views.brokerviewcustomerdeal, name='brokerviewcustomerdeal'),
    path('brokerviewdealerdeal/<int:id>/', views.brokerviewdealerdeal, name='brokerviewdealerdeal'),
    path('dealerviewcustomerdeal/<int:id>/', views.dealerviewcustomerdeal, name='dealerviewcustomerdeal'),
    path('dealerviewdealerdeal/<int:id>/', views.dealerviewdealerdeal, name='dealerviewdealerdeal'),
    path('brokerupdatecustomerstatus/<int:id>/', views.brokerupdatecustomerstatus, name="brokerupdatecustomerstatus"),
    path('brokerpendingdeals/', views.brokerpendingdeals, name="brokerpendingdeals"),
    path('brokernewform/', BrokerNewFormWizard.as_view(), name="brokernewform"),
    path('brokermydeals/', views.brokermydeals, name="brokermydeals"),
    path('brokerupdateform/<int:id>/', BrokerUpdateFormWizard.as_view(), name="brokerupdateform"),
    path('brokerupdatecustomerform/<int:id>/', BrokerUpdateCustomerForm.as_view(), name="brokerupdatecustomerform"),
    path('applicationdetails/<int:id>/', views.applicationdetials, name="applicationdetails"),
    path('myfinancingnewform/', views.myfinancingnewform, name="myfinancingnewform"),
    path('brokercommunication/', views.brokercommunication, name="brokercommunication"),
    path('additionaldocument/', views.additionaldocuments, name="additionaldocuments"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('dealerfinancingform/<int:dealer_id>/', DealerFinancingForm.as_view(), name='dealerfinancingform'),
    path('dealerlandingpage/<int:dealer_id>/', views.DealerLandingPage, name="dealerlandingpage"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)