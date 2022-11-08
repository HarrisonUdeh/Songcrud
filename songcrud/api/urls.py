from django.urls import path
from .views import artiste_list_api, song_list_api, song_detail_api





urlpatterns = [
    path('songs/', song_list_api, name="song_list_api"),
    path('artistes/', artiste_list_api, name="artiste_list_api"), 
    path('songs/<str:title>/', song_detail_api, name = "song_detail_api" )

]