from django.db import models
from django.contrib import admin

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    author = models.CharField(max_length=100)
    copyright = models.CharField(max_length=500, blank=True)
    ccli_number = models.CharField(max_length=50, blank=True)
    original_key = models.CharField(max_length=2, choices=
            (('Ab','Ab'),('A','A'),('Bb','Bb'),
                ('B','B'),('C','C'),('Db','Db'),
                ('D','D'),('Eb','Eb'),('E','E'),
                ('F','F'),('F#','F#'),('Gb','Gb'),('G','G')))
    chords = models.TextField()
    tags = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)

    class SongAdmin(admin.ModelAdmin):
        prepopulated_fields = {"slug": ("title",)}

    def __unicode__(self):
        return self.title

