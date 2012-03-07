from django.shortcuts import render_to_response, get_object_or_404
from songs.models import Song

def detail(request, slug, key):
    object = get_object_or_404(Song, slug=slug)
    return render_to_response('song_detail.html', 
            {'object': object, 'key': key})

