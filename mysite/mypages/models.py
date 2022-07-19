from django.db import models
from django.core.exceptions import ValidationError
import datetime

# Create your models here.

class favegames(models.Model):
    gamename = models.CharField("name of game/series", max_length=100)
    startyear = models.DateField("release year/start of series")

    def __str__(self):
        return self.gamename


class modslist(models.Model):
    modname = models.CharField("name of mod", max_length=100)
    releaseyear = models.DateField("release year/start of series")
    game = models.CharField("name of game", max_length=100)
    link = models.URLField(max_length=200, default="admin/mypages/mods/")
    image = models.ImageField(upload_to="static/images")

    def __str__(self):
        return self.modname
