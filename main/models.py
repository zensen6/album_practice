from django.db import models

# Genre
class Genre(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

# Artist
class Artist(models.Model):
    full_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='artists/',null=True)
    def __str__(self):
        return self.full_name

# Album
class Album(models.Model):
    artist=models.ManyToManyField(Artist)
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='albums/',null=True)
    detail=models.TextField()
    add_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

# Song
class Song(models.Model):
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE,null=True)
    artist=models.ManyToManyField(Artist)
    album=models.ForeignKey(Album,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=100)
    song_src=models.FileField(upload_to='songs/',null=True)
    duration=models.DurationField()
    add_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

# Song Collection
