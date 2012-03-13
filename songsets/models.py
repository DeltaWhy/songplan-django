from django.db import models
from django.contrib import admin
from songplan.songs.models import Song

# Create your models here.
class SongSet(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    songs = models.ManyToManyField(Song, through="SetItem")

    class Meta:
        ordering = ["date","title"]

    @models.permalink
    def get_absolute_url(self):
        return ('set_detail', [self.id])

    def __unicode__(self):
        return self.title

class SetItem(models.Model):
    song = models.ForeignKey(Song)
    songSet = models.ForeignKey(SongSet)
    index = models.IntegerField();

    class Meta:
        ordering = ['songSet', 'index']

    def __unicode__(self):
        return self.song.__unicode__()
