from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('sign-in/', views.signin, name="sign-in"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('newform/', views.newform, name="newform"),
    path('mydeals/', views.mydeals, name="mydeals"),
    path('pendingdeals/', views.pendingdeals, name="pendingdeals"),
    path('updateform/<int:id>/', views.updateform, name="updateform"),
    #path('dealerpendingdeals/', views.dealerpendingdeals, name="dealerpendingdeals"),
    #path('dealermydeals/', views.dealermydeals, name="dealermydeals"),
    path('dealernewform/', views.dealernewform, name="dealernewform"),
]