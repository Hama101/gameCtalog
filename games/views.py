from django.shortcuts import render
from django.http import HttpResponse
from .models import Games

def home(request):
    return render(request,'base.html')

def games(request):
    games = Games.objects.all()
    dict = {"games" : games}
    return render(request , 'games.html',dict)

def game(response  , id):
    game = Games.objects.get(id=id)
    dict = {'game' : game}
    return render(response , 'game.html' , dict)

def findGame(request):
    title = request.POST["Search"]
    game = Games.objects.filter(title=title)
    dict = {"game" : game}
    return render(request,'foundGame.html' , dict)