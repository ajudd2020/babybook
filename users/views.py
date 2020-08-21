from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegistrationForm

# Create your views here.

def register(response):

    if response.method=="POST":
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')
    else:
        form = RegistrationForm()

    return render(response, "registration/register.html", {"form":form})