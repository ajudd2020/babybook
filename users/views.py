from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegistrationForm, CustomUserForm

from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.




def register(request):

    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            print("Not valid")

    else:
        form = RegistrationForm()


    return render(request, "registration/register.html", {"form":form})

'''
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST.get('username')
        email = request.POST['email']
        baby_name = request.POST['baby_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            print("First Check")
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return(redirect('register'))
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return(redirect('/'))
            else:
                user = User.objects.create_user(username=request.POST.get('username'), password=password1, email=email, first_name=first_name, last_name=last_name, baby_name=baby_name)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Password doesn't match")
            return(redirect('/'))


    else:
        return render(request, 'registration/register.html')
'''