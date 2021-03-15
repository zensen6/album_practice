from django.contrib import admin
from .models import *
from django.utils.html import mark_safe

# genre
admin.site.register(Genre)
# Album
admin.site.register(Album)
# Artist
class ArtistAdmin(admin.ModelAdmin):
    readonly_fields = ('artist_image',)
    def artist_image(obj):
        return obj.artist_image
admin.site.register(Artist)
# Song
admin.site.register(Song)
