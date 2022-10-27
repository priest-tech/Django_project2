from django.contrib import admin

from .models import Artiste

admin.site.register(Artiste)

from .models import Song

admin.site.register(Song)

from .models import Lyric

admin.site.register(Lyric)

# Register your models here.
