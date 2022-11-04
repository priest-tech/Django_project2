from django.urls import include, path

from rest_framework import routers

from musicapp.views import SongViewSet, ArtisteViewSet, LyricViewSet

router = routers.DefaultRouter()
router.register(r'song', SongViewSet)
router.register(r'artiste', ArtisteViewSet)
router.register(r'lyric', LyricViewSet)


urlpatterns = [
    path('', include(router.urls)),
    ]
    # ] + router.urls path('artiste/<int: pk>', ArtisteView.as_view(), name='artiste')
