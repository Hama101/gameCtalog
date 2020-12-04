from django.urls import path
from django.conf.urls import url
from . import views as v

urlpatterns = [
    path('',v.home ),
    path('games/',v.games ),
    path('games/<int:id>', v.game),
    url(r'^findGame', v.findGame, name='findGame'),
    #path('new/',v.new)
]