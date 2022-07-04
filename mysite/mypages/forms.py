from django import forms
from django.forms import ModelForm
from .models import favegames, modslist

class FavegamesForm(forms.Form):
    game_name = forms.CharField(label='Game Name', max_length=100)
    release_year = forms.DateField(label='release year/start of series')