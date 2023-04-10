from django.urls import path
from app import views


urlpatterns = [ 
               
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup,name="signup"),
    path('welcome/', views.welcome,name="welcome"),
    
    ]
