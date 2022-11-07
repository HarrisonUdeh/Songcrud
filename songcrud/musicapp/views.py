from django.shortcuts import render
from django.http import HttpResponse
from .models import Artiste,Song,Lyric

# Create your views here.


def index(request):
    artists = Artiste.objects.all()
    print(artists)
    context ={}
    context = {"artists": artists}
    return render(request, 'musicapp/list_Artistes.html', context)

def artist_detail_pages(request, primary_key):
    artists = Artiste.objects.get(primary_key = primary_key)
    context = {"artists": artists}
    return render(request, 'musicapp/artist_detail.html', context)
def index2(request):
    return HttpResponse("Welcome to my music app")
