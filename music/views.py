from django.shortcuts import render
from django.http import HttpResponse
from  django.http import  Http404
# from django.template import loader

from music.models import Album 


# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    # template   = loader.get_template('music/index.html')
    context    = {
        "all_albums" :all_albums,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html', context)


def detail(request, id):
    try:
        album = Album.objects.get(pk=id)
        songs = album.song_set.all()
        context =  {
            "album":album,
            "songs":songs
        }
    except Album.DoesNotExist:
        raise Http404("Album does not exist")    
    return render(request, 'music/detail.html',context) 


