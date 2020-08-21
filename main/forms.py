from django import forms
from .models import BabyBookEntry

class CreateEntryForm(forms.ModelForm):
    class Meta:
        model = BabyBookEntry
        fields = ['title', 'entry', 'main_image']

