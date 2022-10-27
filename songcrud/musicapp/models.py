from django.db import models
from datetime import datetime


class Artiste(models.Model):
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    age= models.IntegerField()
    
    def __str__(self):
        return self.first_name
    

class Song(models.Model):
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_released= models.DateTimeField()
    likes = models.IntegerField(default=0)
    artist_id = models.IntegerField()
    
    def __str__(self):
        return self.title
    

class Lyric(models.Model):
    artiste = models.ForeignKey(Artiste,on_delete=models.CASCADE)
    content = models.TextField()
    song_id = models.IntegerField()
    
    def __str__(self):
        return self.song_id
       
# Create your models here.
