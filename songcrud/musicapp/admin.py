from django.contrib import admin
from .models import Artiste, Song, Lyric
# Register your models here.

# admin.site.register(Artiste)
@admin.register(Artiste)
class ArtisteAdmin(admin.ModelAdmin):
    list_display = ['artist_name', 'first_name', 'last_name', 'age', 'primary_key']
admin.site.register(Song)
admin.site.register(Lyric)
