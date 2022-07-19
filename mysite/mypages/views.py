from django.shortcuts import render
from django.contrib import messages
from django.http.response import HttpResponse
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
            modslResp= ['<body style="background-color:black;"><h2 style="color:white;">Mod entry successfully added to list</h3><br /><a href="http://localhost:8000/mypages/favouritegames">Return to list</a>']
            return HttpResponse(modslResp)
        else:
            modslResp = ['<body style="background-color:black;"><h2 style="color:white;">Mod entry was unsuccessful, please verify form entries are valid</h3><br /><a href="http://localhost:8000/mypages/favouritegames">Try again</a>']
            return HttpResponse(modslResp)

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
            favgamesResp= ['<body style="background-color:black;"><h2 style="color:white;">Game entry successfully added to list</h3><br /><a href="http://localhost:8000/mypages/favouritegames">Return to list</a>']
            return HttpResponse(favgamesResp)
        else:
            favgamesResp = ['<body style="background-color:black;"><h2 style="color:white;">Game entry was unsuccessful, please verify form entries are valid</h3><br /><a href="http://localhost:8000/mypages/favouritegames">Try again</a>']
            return HttpResponse(favgamesResp)

    favegames_form = favegamesform()
    gamenames = favegames.objects.all
    return render(
        request=request,
        template_name="mypages/favouritegames.html",
        context={"favegames_form": favegames_form, "game_names": gamenames},
    )
