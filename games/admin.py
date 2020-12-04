from django.contrib import admin
from .models import *


class GamesAdmin(admin.ModelAdmin):
    list_display = ('title' , 'category','price' ,
                    'os' , 'cpu' , 'gpu' , 'ram' , 'hdd',
                    'shortDescription' ,
                    'longDescription' , 'coverImg' ,
                    'img1Url' , 'img2Url' ,'img3Url',
                    'img4Url' , 'img5Url' ,'img6Url' , 'youtubeUrl')

admin.site.register(Games,GamesAdmin)