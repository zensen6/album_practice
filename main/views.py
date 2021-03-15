from django.shortcuts import render
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from .models import *
from django.db.models import Count
# Create your views here.
def index(request):

    if 'q' in request.GET:
        q=request.GET['q']
        songs=Song.objects.filter(title__icontains=q).order_by('-id')
    else:
        songs=Song.objects.all().order_by('-id')
    return render(request,'index.html',{
        'songs':songs
    })

# Albums
def albums(request):
    return render(request,'albums.html',{
        'albums':Album.objects.all()
    })
# Album
def album(request,id):
    album=Album.objects.get(pk=id)
    return render(request,'album.html',{
        'album':album,
        'songs':Song.objects.filter(album=album).order_by('-id'),
        'count_songs':Song.objects.filter(album=album).count()
    })

# Artists
def artists(request):
    return render(request,'artists.html',{
        'artists':Artist.objects.all()
    })
# Artist
def artist(request,id):
    artist=Artist.objects.get(pk=id)
    return render(request,'artist.html',{
        'artist':artist,
        'songs':Song.objects.filter(artist=artist).order_by('-id'),
        'count_songs':Song.objects.filter(artist=artist).count()
    })


# Genres
def genres(request):
    return render(request,'genres.html',{
        'genres':Genre.objects.all()
    })
# Genre
def genre(request,id):
    genre=Genre.objects.get(pk=id)
    return render(request,'genre.html',{
        'genre':genre,
        'songs':Song.objects.filter(genre=genre).order_by('-id'),
        'count_songs':Song.objects.filter(genre=genre).count()
    })

# My Collection
def my_collection(request):
    songs=Song.objects.all()
    return render(request,"my-collection.html",{
        'songs':songs
    })


