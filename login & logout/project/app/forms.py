import email
from django import forms
from django.contrib.auth.models import User
from .models import Details
from django.contrib.auth.models import UsercreationForm


class NewuserForm(UsercreationForm):
    email = forms.EmailField(required=True) 
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
   # def create(self,validated_data):
       # user = User.objects.create_user(** validated_data)
        #return user
    # we have create a Multiple users in User Models....