from django import forms
from django.forms import ModelForm, TextInput, DateInput
from django.core.exceptions import ValidationError
from .models import favegames, modslist



class favegamesform(ModelForm):
    class Meta:
        model = favegames
        fields = ["gamename", "startyear"]

class modslistform(ModelForm):
    class Meta:
        model = modslist
        fields = ["modname", "releaseyear", "game", "link", "image"]
