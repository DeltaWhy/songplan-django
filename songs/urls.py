from django.conf.urls.defaults import patterns, include, url
from songplan.songs.models import Song

info_dict = {
    'queryset': Song.objects.all(),
}

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', dict(info_dict, template_name="songs_list.html")),
    url(r'^(?P<slug>[-\w]+)/$', 'django.views.generic.list_detail.object_detail',
        dict(info_dict, slug_field='slug', template_name="song_detail.html")),
    url(r'^(?P<slug>[-\w]+)/(?P<key>[-\w]+)/$', 'songs.views.detail'),
)
