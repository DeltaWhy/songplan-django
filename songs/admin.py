from songs.models import Song
from django.contrib import admin

class SongAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    class Media:
        css = {"all": ("admin/css/song_styles.css",)}

admin.site.register(Song, SongAdmin)
