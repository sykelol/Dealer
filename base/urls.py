from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('sign-in/', views.signin, name="sign-in"),
    path('logout/', views.logoutUser, name="logout"),
    path('sign-in/register', views.register, name="register"),
]