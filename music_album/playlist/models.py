from django.contrib import admin
from django.db import models
from catalog.models import Track
# Create your models here.
class Playlist(models.Model):
    playlist_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    track = models.ForeignKey(Track, unique=True)

    class Meta:
        ordering = ['date_added']

    def name(self):
        return self.track.name

admin.site.register(Playlist)