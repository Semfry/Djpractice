from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'mypages'
urlpatterns = [
    path('', views.index, name='index'),
    path('mods', views.modspage, name='mods'),
    path('favouritegames', views.favouritegames, name='favouritegames'),
]