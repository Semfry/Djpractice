from django.shortcuts import render, redirect
from django.contrib import messages

from .models import favegames, modslist
from .forms import favegamesform, modslistform

# Create your views here.

def index(request):
    return render(request, 'mypages/mainpage.html')

def modspage(request):
    modsnames = modslist.objects.all
    context = {'mod_name': modsnames}
    return render(request, 'mypages/mods.html', context)

def favouritegames(request):
    if request.method == 'POST':
        favegames_form = favegamesform(request.POST, request.FILES)
        if favegamesform.is_valid():
            favegamesform.save()
            messages.success(request, ('Saved successfully!'))
        else:
            messages.error(request, ('Error'))

        return redirect("mypages/favouritegames.html")
    
    favegames_form = favegamesform()
    gamenames = favegames.objects.all
    return render(request=request, template_name='mypages/favouritegames.html', context={'favegames_form':favegames_form, 'game_names':gamenames })

