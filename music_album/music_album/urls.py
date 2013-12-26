from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^index/$', 'catalog.views.home'),
    url(r'^index/all_tracks/$', 'catalog.views.all_tracks'),
    url(r'^index/all_tracks/(?P<track_slug>[-\w]+)/$', 'catalog.views.tracks'),
    url(r'^index/all_albums/$', 'catalog.views.all_albums'),
    url(r'^index/all_albums/(?P<album_slug>[-\w]+)$', 'catalog.views.allalbums'),
    url(r'^index/artists/$', 'catalog.views.artists'),
    url(r'^index/artists/(?P<artist_slug>[-\w]+)/$', 'catalog.views.in_artist'),
    # url(r'^music_album/', include('music_album.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # for authentication
    url(r'^accounts/login/$', 'catalog.views.login'),
    url(r'^accounts/auth/$','catalog.views.auth_view'),
    url(r'^accounts/logout/$', 'catalog.views.logout'),
    url(r'^accounts/loggedin/$', 'catalog.views.loggedin'),
    url(r'^accounts/invalid/$', 'catalog.views.invalid_login'),
    url(r'^accounts/register/$', 'catalog.views.register_user'),
    #url(r'^accounts/register_success/$', 'catalog.views.register_success'),

    # for playlist
    url(r'^playlist/$', 'playlist.views.show_playlist'),
)

