from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.index,name='index'),
    path('genres',views.genres,name='genres'),
    path('genre/<int:id>',views.genre,name='genre'),
    path('albums',views.albums,name='albums'),
    path('album/<int:id>',views.album,name='album'),
    path('artists',views.artists,name='artists'),
    path('artist/<int:id>',views.artist,name='artist'),
    path('my-collection',views.my_collection,name='my-collection'),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 