from django.contrib import admin

from .models import favegames, modslist

# Register your models here.

admin.site.register(favegames)
admin.site.register(modslist)