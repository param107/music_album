from django.shortcuts import get_object_or_404, render_to_response,render
from django.template import RequestContext, loader,Context
from models import Album, Artist, Track
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from forms import PlaylistForm
from playlist import playlist


def home(request):
    albums = Album.objects.all()[:5]
    artists = Artist.objects.filter(is_famous = True)
    tracks = Track.objects.all() [:15]  
    return render_to_response('home.html',locals(),
                                  context_instance=RequestContext(request))    
    
def all_tracks(request):
    tracks = Track.objects.all()
    return render_to_response('all_tracks.html',locals(),
                                      context_instance=RequestContext(request))    
def all_albums(request):
    tracks = Album.objects.all()
    return render_to_response('all_albums.html',locals(),
                                      context_instance=RequestContext(request))
def allalbums(request, album_slug):
    tracks = get_object_or_404(Album, link=album_slug)
    return render_to_response('allalbums.html',locals(),
                                      context_instance=RequestContext(request))

def artists(request):
    tracks = Artist.objects.all()
    return render_to_response('artists.html',locals(),
                                      context_instance=RequestContext(request))
def in_artist(request, artist_slug):
    tracks = get_object_or_404(Artist, link=artist_slug)
    return render_to_response('allartists.html',locals(),
                                      context_instance=RequestContext(request))
def tracks(request, track_slug):
    track = get_object_or_404(Track, link = track_slug)
    art = track.artist.all()
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = PlaylistForm(request, postdata)
        if form.is_valid():
            playlist.add_playlist(request)
        return HttpResponseRedirect('/playlist')
    else:
        form = PlaylistForm(request=request, label_suffix=':')
        form.fields['track_slug'].widget.attrs['value'] = track_slug
        request.session.set_test_cookie()



    return render_to_response('tracks.html',locals(),
                                          context_instance=RequestContext(request))    
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html',locals(),
                                              context_instance=RequestContext(request))
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')
    
def loggedin(request):
    return render_to_response('loggedin.html')
def invalid_login(request):
    return render_to_response('invalid.html')
def logout(request):
    return render_to_response('logout.html')
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.Post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = UserCreationForm()
    return render_to_response('register.html', args)