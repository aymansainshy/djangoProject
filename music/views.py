from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from  django.http import  Http404
# from django.template import loader

from music.models import Album, Song 


# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    # template   = loader.get_template('music/index.html')
    # return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html', {"all_albums" :all_albums})


def detail(request, id):
    # try:
        # album = Album.objects.get(pk=id)
    album = get_object_or_404(Album,pk=id)
    # songs = album.song_set.all()
    # except Album.DoesNotExist:
        # raise Http404("Album does not exist")    
    return render(request, 'music/detail.html', {
            "album":album,
            # "songs":songs
        }) 


def favorite(request, id):
    album = get_object_or_404(Album, pk=id)

    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
        # songs = album.song_set.all()
        print('Song id dddd' + request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request,  'music/detail.html',{
            'album' : album,
            'error_massege': 'YOU DID NOT SELECT ANY SONG',
        })   
    else:     
        if selected_song.is_favorite:
            selected_song.is_favorite = False
            selected_song.save()
        else:
            selected_song.is_favorite = True
            selected_song.save()
    return render(request, 'music/detail.html',{
            'album': album,
         })   

