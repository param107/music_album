# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from playlist import *
def show_playlist(request):
    playlist_no = count_playlist(request)
    playlist = get_playlist(request)
    return render_to_response('playlist.html', locals(),
                              context_instance=RequestContext(request))
