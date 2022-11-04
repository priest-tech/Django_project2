from django.contrib import admin

from .models import Artiste

admin.site.register(Artiste)
class ArtisteAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_filter =['last_name']

from .models import Song

admin.site.register(Song)
class SongAdmin(admin.ModelAdmin):
     list_display = ['title', 'date_released']

from .models import Lyric

admin.site.register(Lyric)

# Register your models here.
