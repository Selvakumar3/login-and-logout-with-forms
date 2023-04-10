from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.db import IntegrityError

# sign in function 
def signnewuser(request):
    if request.method=="POST":
        if request.POST.get('password1')==request.POST.get('password2'):
            try:
                saveuser= User.objects.create_user(request.POST.get('username'),password=request.POST.get('password'))
                saveuser.save() 
                return render(request,'signup.html',{'form':UserCreationForm(),'info':'The user' + request.POST.get('username')})  
            except IntegrityError:
                return render(request,'signup.html'),{'form':UserCreationForm(),'error':'The user' + request.POST.get('username')}
        else:
            return render(request,'signup.html',{'form':UserCreationForm(),'error':'The password are not match'})
    else:
        return render(request,'signup.html',{'form':UserCreationForm})    
 
 
# login function 
                
def loginuser(request):
    if request.method=="POST":
        loginsuccess = authenticate(request, username=request.POST.get('username'),password=request.POST.get('password'))                 
        if loginsuccess is None:
            return render(request,'login.html',{'form':AuthenticationForm(),'error':'The username and password are wrong'})
        else:
            login(request,loginsuccess)
            return redirect('home')
    else:
        return render(request,'login.html',{'form':AuthenticationForm()})

# homepage function

def home(request):
    return render(request,'welcome.html')

# logout function

def logout(request):
    return redirect('loginuser')       
            
                                                 
                                                          