import datetime
from django.shortcuts import render
from django.template import Template,Context



def mainPage(request):
    template = 'home.html'
    return render(request,template)