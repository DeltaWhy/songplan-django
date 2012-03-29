from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from songs.models import Song
from songsets.models import *
from songplan.songs import helpers
def music(request, object_id):
    songset = get_object_or_404(SongSet, pk=object_id)
    songs = []
    for item in songset.setitem_set.all():
        chords = helpers.transpose(item.song.original_key, item.key, item.song.chords)
        headerlines = helpers.headerlines(chords)
        songs.append({'song': item.song, 'key': item.key, 'chords': chords, 
                    'headerlines': headerlines})
    return render_to_response('set_music.html', {'songs': songs})
