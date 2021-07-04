from django.shortcuts import render
from .models import *

# Create your views here.
def peoplePage(request):
    template = 'peoples.html'
    context = {'peoples': People.objects.all(),
               'person.name':People.name,
               'person.race':People.race,
               'person.description':People.description
    }
    return render(request,template,context)

def recapPage(request):
    template = 'recaps.html'
    context = {'recaps': Recap.objects.all(),
               'recap.date':Recap.date,
               'recap.description':Recap.description
    }
    return render(request,template,context)

def monsterPage(request):
    template = 'monsters.html'
    context = {'Monsters': Monster.objects.all(),'monster.name':Monster.name,'monster.type':Monster.type,'monster.description':Monster.description
    }
    return render(request,template,context)

def itemsPage(request):
    template = 'items.html'
    context = {'items':Item.objects.all(),'items.name':Item.name,'item.description':Item.description}
    return render(request,template,context)

def enemySearch(request):
    monsterName = request.GET['enemyName']
    searchedEnemy = Monster.objects.get(name__iexact=monsterName)
    template = 'enemySearch.html'
    context = {
        'monsterName':searchedEnemy.name,
        'monsterDescription':searchedEnemy.description,
    }
    return render(request,template,context)

