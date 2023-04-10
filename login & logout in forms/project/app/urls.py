from django.urls import path
from app import views

urlpatterns = [ 
    path('sign/',views.signnewuser, name="signnewuser"),
    path('',views.loginuser, name="loginuser"),
    path('welcome/',views.home, name="home"),
    path('logout/',views.logout, name="logout"),
    ]
