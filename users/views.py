from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegistrationForm

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

