from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length = 255)
    last_name=forms.CharField(max_length = 255)


    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

