from django.shortcuts import render, redirect
from django.contrib import messages

from .models import favegames, modslist
from .forms import favegamesform, modslistform

# Create your views here.


def index(request):
    return render(request, "mypages/mainpage.html")


def modspage(request):
    if request.method == "POST":
        modslist_form = modslistform(request.POST, request.FILES)
        if modslist_form.is_valid():
            modslist_form.save()
            messages.success(request, ("Saved successfully!"))
        else:
            messages.error(request, ("Error"))

    modslist_form = modslistform()
    modsnames = modslist.objects.all
    return render(
        request=request,
        template_name="mypages/mods.html",
        context={"modslist_form": modslist_form, "mod_names": modsnames},
    )


def favouritegames(request):
    if request.method == "POST":
        favegames_form = favegamesform(request.POST, request.FILES)
        if favegames_form.is_valid():
            favegames_form.save()
            messages.success(request, ("Saved successfully!"))
        else:
            messages.error(request, ("Error"))

    favegames_form = favegamesform()
    gamenames = favegames.objects.all
    return render(
        request=request,
        template_name="mypages/favouritegames.html",
        context={"favegames_form": favegames_form, "game_names": gamenames},
    )
