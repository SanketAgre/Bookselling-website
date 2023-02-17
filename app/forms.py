from django.contrib.auth.forms import UserCreationForm  
from .models import User
from django import forms
from django.core.validators import RegexValidator 

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Username'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Email'}))
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Phone No'}), validators=[phone_regex], max_length=17)
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Confirm Password'}))

    class Meta:
        model=User
        fields=['username', 'email','phone', 'password1', 'password2']
