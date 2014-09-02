from django.conf.urls.defaults import patterns, include, url
from songplan.songs.models import Song

info_dict = {
    'queryset': Song.objects.all(),
}

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', dict(info_dict, template_name="songs_list.html")),
    url(r'^json/$', 'songs.views.list_json'),
    url(r'^(?P<slug>[-\w]+)/$', 'songs.views.detail', {'key': ''}, name='song_view'),
    url(r'^(?P<slug>[-\w]+)/lyrics/$', 'songs.views.lyrics'),
    url(r'^(?P<slug>[-\w]+)/json/$', 'songs.views.detail_json'),
    url(r'^(?P<slug>[-\w]+)/(?P<key>[A-G][+-]?)/$', 'songs.views.detail', name='transpose_view'),
    url(r'^(?P<slug>[-\w]+)/nashville/$', 'songs.views.detail', {'key': 'nashville'}, name='nashville_view'),
)
