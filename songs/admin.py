from songs.models import Song
from django.contrib import admin

class SongAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Song, SongAdmin)
