from rest_framework import serializers
from musicapp.models import Artiste, Song, Lyric

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ["artist_name", "first_name", "last_name", "primary_key"]
    

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["artiste_id", "title", "date_released"]


    