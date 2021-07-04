"""Defines URL patterns for learning_logs."""
from django.urls import path

from . import views

app_name = 'dndWiki'
urlpatterns = [
       # Home page
    path('peoples/',views.peoplePage,name='people'),
    path('recaps/',views.recapPage,name='recap'),
    path('monsters/',views.monsterPage,name='monster'),
    path('items/',views.itemsPage,name='items'),
    path('enemySearch/',views.enemySearch,name='enemySearch'),
   ]