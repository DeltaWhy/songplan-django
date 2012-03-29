from django.conf.urls.defaults import patterns, include, url
from songplan.songsets.models import SongSet

info_dict = {
    'queryset': SongSet.objects.all(),
}

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', dict(info_dict, template_name="sets_list.html")),
    url(r'^(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail',
        dict(info_dict, template_name="set_detail.html"), name='set_detail'),
    url(r'^(?P<object_id>[\d]+)/music/$', 'songsets.views.music', name='set_music_view'),
    #url(r'^(?P<slug>[-\w]+)/(?P<key>[A-G][+-]?)/$', 'songs.views.detail'),
)
