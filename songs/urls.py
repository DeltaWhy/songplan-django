from django.conf.urls.defaults import patterns, include, url
from songplan.songs.models import Song

info_dict = {
    'queryset': Song.objects.all(),
}

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', dict(info_dict, template_name="songs_list.html")),
    url(r'^(?P<slug>[-\w]+)/(?P<key>)$', 'songs.views.detail'),
    url(r'^(?P<slug>[-\w]+)/(?P<key>[A-G][+-]?)/$', 'songs.views.detail'),
)
