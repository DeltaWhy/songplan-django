from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from songs.models import Song
from songplan.songs import helpers
import simplejson

def detail(request, slug, key):
    key = key.replace('-','b').replace('+','#')
    song = get_object_or_404(Song, slug=slug)
    if key == '':
        chords = song.chords
        key = song.original_key
    else:
        chords = helpers.transpose(song.original_key, key, song.chords)
    headerlines = helpers.headerlines(chords)
    return render_to_response('song_detail.html', 
            {'song': song, 'key': key, 'chords': chords, 
                'headerlines': headerlines})

def lyrics(request, slug):
    song = get_object_or_404(Song, slug=slug)
    lyrics = helpers.lyrics(song.chords)
    headerlines = helpers.headerlines(lyrics)
    return render_to_response('song_detail.html',
            {'song': song, 'key': 'Lyrics', 'chords': lyrics,
                'headerlines': headerlines})

def list_json(request):
    songs = Song.objects.all()
    result = {}
    for song in songs:
        result[song.title] = request.build_absolute_uri(song.get_absolute_url()) + "json/"
    return HttpResponse(simplejson.dumps(result))

def detail_json(request, slug):
    song = get_object_or_404(Song, slug=slug)
    result = {"title": song.title, "author": song.author, "copyright":
            song.copyright, "lyrics": helpers.splitlyrics(song.chords),
            "order": []}
    return HttpResponse(simplejson.dumps(result))
