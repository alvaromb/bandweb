from django.db import models
from django.contrib.auth.models import User

# Models for the user and content sections
class Categorie(models.Model):
    name = models.CharField(max_length=100)

class News(models.Model):
    title = models.CharField(max_length=350)
    pub_date = models.DateTimeField()
    content = models.TextField()
    categorie = models.ForeignKey(Categorie)
    author = models.ForeignKey(User)

class Album(models.Model):
    title = models.CharField(max_length=1000)
    rel_date = models.DateTimeField()
    tracks = models.PositiveSmallIntegerField()
    art = models.ImageField(upload_to='art/%Y/%m')

class Track(models.Model):
    title = models.CharField(max_length=1000)
    lyrics = models.TextField(blank=True)
    duration = models.TimeField(null=True)
    album = models.ForeignKey(Album)

class Tour(models.Model):
    name = models.CharField(max_length=500)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField(blank=True)
    
class Show(models.Model):
    date = models.DateTimeField()
    location = models.CharField(max_length=300)
    venue = models.CharField(max_length=300)
    info = models.TextField(blank=True)
    headline = models.NullBooleanField()
    tour = models.ForeignKey(Tour, null=True)

class Journal(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    text = models.TextField()
    tour = models.ForeignKey(Tour)

class Biography(models.Model):
    text = models.TextField()
    hometown = models.CharField(max_length=300)
    genre = models.CharField(max_length=300)
    label = models.CharField(max_length=300)

class PhotoAlbum(models.Model):
    name = models.CharField(max_length=300)
    summary = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Photo(models.Model):
    title = models.CharField(max_length=256)
    summary = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='photos/%Y/%m')
    photo_album = models.ForeignKey(PhotoAlbum, null=True)
    is_cover_photo = models.BooleanField()

class Discussion(models.Model):
    reply_to = models.ForeignKey("self", null=True)
    text = models.TextField()
    autor = models.ForeignKey(User)
    
class Comment(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    news = models.ForeignKey(News, null=True)
    album = models.ForeignKey(Album, null=True)
    show = models.ForeignKey(Show, null=True)

