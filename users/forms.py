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

class CustomUserForm (forms.Form):
    username = forms.CharField(max_length = 255)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        print("email")
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username
    
    def clean_password2(self):
        print("TEST")
        password1 = self.cleaned_data.get('password1')
        print(password1, "1")

        password2 = self.cleaned_data.get('password2')
        print(password2, "2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")


        return password2
    
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['email'],
            self.cleaned_data['username'],
            self.cleaned_data['password1'],
        )
        return user