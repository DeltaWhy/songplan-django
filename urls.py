from django.conf.urls.defaults import patterns, include, url
from songplan import songs, songsets

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'songplan.views.home', name='home'),
    # url(r'^songplan/', include('songplan.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^$', 'django.views.generic.simple.redirect_to', {'url': '/songs/'}),
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^songs/', include('songplan.songs.urls')),
    url(r'^sets/', include('songplan.songsets.urls')),
    url(r'^openid/', include('django_openid_auth.urls')),
)

LOGIN_URL = '/openid/login/'
LOGIN_REDIRECT_URL = '/'
