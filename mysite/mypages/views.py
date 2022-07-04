from datetime import date
from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect

from .models import favegames, modslist
from .forms import FavegamesForm

# Create your views here.

def index(request):
    return render(request, 'mypages/mainpage.html')

def modspage(request):
    modsnames = modslist.objects.all
    context = {'mod_name': modsnames}
    return render(request, 'mypages/mods.html', context)

def favouritegames(request):
    gamenames = favegames.objects.all
    context = {'game_name': gamenames}
    if request.method == 'POST':
        form = FavegamesForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = FavegamesForm()
    return render(request, 'mypages/favouritegames.html', context, {'FavouriteGames' : form})
    

