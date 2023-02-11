from django.urls import path
from . import views
from .views import NewFormWizard, CustomerFinancingWizard
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
    path('newform/', NewFormWizard.as_view(), name="newform"),
    path('mydeals/', views.mydeals, name="mydeals"),
    path('pendingdeals/', views.pendingdeals, name="pendingdeals"),
    path('updateform/<int:id>/', views.updateform, name="updateform"),
    path('updatestatus/<int:id>/', views.updatestatus, name="updatestatus"),
    path('dealernewform/', views.dealernewform, name="dealernewform"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)