from django.shortcuts import render

def home(request):
    return render(request,'base.html')

def games(request):
    return render(request , 'games.html')
