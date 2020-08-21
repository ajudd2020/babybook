from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BabyBookEntry
from .forms import CreateEntryForm


# Create your views here.
def home (response):
    return render(response, 'main/home.html', {})

def about (response):
    return render(response, 'main/about.html', {})

class CreateEntryView(LoginRequiredMixin, CreateView):
    model = BabyBookEntry
    fields = ['title', 'entry', 'main_image']
    template_name = 'main/entry.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EntryListView(ListView):
    model = BabyBookEntry
    template_name='main/view.html'
    ordering = ['-post_date']

class EditPostView(UpdateView):
    model = BabyBookEntry
    form_class = CreateEntryForm
    template_name = 'main/edit_post.html'

def index(response):
    user_entry = BabyBookEntry.objects.all
    print(user_entry)