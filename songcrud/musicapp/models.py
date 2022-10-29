from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(
        max_length=50, help_text='Enter your first name', default="name")
    last_name = models.CharField(
        max_length=50, help_text='Enter your last name', default="name")
    age = models.IntegerField(validators=[MinValueValidator(
        18.0), MaxValueValidator(120.0)], help_text='Enter your age', default=18)
    primary_key = models.BigAutoField(primary_key=True)
    #primary_key = models.BigAutoField(primary_key= True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Song(models.Model):
    # artiste_id = models.ForeignKey(
    #    Artiste.primary_key, on_delete=models.CASCADE)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="song")
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Lyric(models.Model):
    content = models.TextField(max_length=1000000, default="lyrics")
    #song_id = models.ForeignKey(Song.artiste_id, on_delete=models.CASCADE)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
