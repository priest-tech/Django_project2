from rest_framework import serializers
from musicapp.models import Song, Artiste, Lyric

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        
class ArtisteSerializer(serializers.ModelSerializer):
     class Meta:
         model = Artiste           
         fields = '__all__'
         
class LyricSerializer(serializers.ModelSerializer):
    # song_id = SongSerializer(many=True)
    
    class Meta:
         model = Lyric           
         fields = '__all__'     