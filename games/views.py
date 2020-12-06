from django.shortcuts import render
from django.http import HttpResponse
from .models import Games
from .filters import Filters

def home(request):
    return render(request,'base.html')


def games(request):
    games = Games.objects.filter().order_by('title')

    myFilter = Filters(request.GET ,
                        queryset=games)
    games = myFilter.qs

    context = {
        'myFilter' : myFilter ,
        'games' : games
    }

    return render(request , 'games.html' , context)


def game(response  , id):
    game = Games.objects.get(id=id)
    dict = {'game' : game}
    return render(response , 'game.html' , dict)

