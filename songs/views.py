from django.shortcuts import render_to_response, get_object_or_404
from songs.models import Song
from songplan.songs import helpers

def detail(request, slug, key):
    key = key.replace('-','b').replace('+','#')
    song = get_object_or_404(Song, slug=slug)
    if key == '':
        chords = song.chords
        key = song.original_key
    else:
        chords = helpers.transpose(song.original_key, key, song.chords)
    return render_to_response('song_detail.html', 
            {'song': song, 'key': key, 'chords': chords})

