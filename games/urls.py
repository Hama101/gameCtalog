from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.home ),
    #path('games/',v.games ),
    #path('games/<str:title>', v.games)
    #path('new/',v.new)
]