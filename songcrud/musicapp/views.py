# from django.http import HttpResponse
# from django.shortcuts import render
# from django.http import JsonResponse

# def index(request):
# # # def musicappOverview(request):
#     return JsonResponse("MUSICAPP BASE POINT", safe=False)
# return HttpResponse("Hello, world. This is my Djang app.")

from rest_framework import viewsets

from musicapp.serializers import ArtisteSerializer, SongSerializer, LyricSerializer
from musicapp.models import Song, Artiste, Lyric


class ArtisteViewSet(viewsets.ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class LyricViewSet(viewsets.ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = LyricSerializer


# class UpdateDeletePostView(
#         UpdateModelMixin,
#         DeleteModelMixin,
#         GenericAPIView):
