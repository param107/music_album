from models import Playlist
from catalog.models import Track
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

import random
P_SESSION_KEY = 'playlist_id'

def _playlist_id(request):
    if request.session.get(P_SESSION_KEY, '') =='':
        request.session[P_SESSION_KEY] = _generate_playlist_id()
    return request.session[P_SESSION_KEY]


def _generate_playlist_id():
    playlist_id = ''
    char =  'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()'
    playlist_id_length = 50
    for y in range(playlist_id_length):
        playlist_id += char[random.randint(0, len(char)-1)]
    return playlist_id

def get_playlist(request):
    return Playlist.objects.filter(playlist_id=_playlist_id(request))

def add_playlist(request):
    postdata = request.POST.copy()
    track_slug = postdata.get('track_slug', '')
    p = get_object_or_404(Track, link = track_slug)
    playlist_list = get_playlist(request)
    track_in_playlist = False

    for list in playlist_list:
        if list.track.id == p.id :

            track_in_playlist = True
        if not track_in_playlist:
            ci = Playlist()
            ci.track = p
            ci.playlist_id = _playlist_id(request)
            ci.save()

def count_playlist(request):
    return get_playlist(request).count()










