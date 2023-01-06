from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('financingform/', views.financingform, name="financingform"),
    path('personal-information/', views.personal_information, name="personal_information"),
    path('employment-information/', views.employment_information, name="employment_information"),
    path('success/', views.successmessage, name="successmessage"),
    path('sign-in/', views.signin, name="sign-in"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('newform/', views.newform, name="newform"),
    path('mydeals/', views.mydeals, name="mydeals"),
    path('pendingdeals/', views.pendingdeals, name="pendingdeals"),
    path('updateform/<int:id>/', views.updateform, name="updateform"),
    path('updatestatus/<int:id>/', views.updatestatus, name="updatestatus"),
    path('dealernewform/', views.dealernewform, name="dealernewform"),
]