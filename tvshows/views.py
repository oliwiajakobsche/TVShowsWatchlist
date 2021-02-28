from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.template import loader
from .models import TvShow

def index(request):
    tvShowsList = TvShow.objects.all()
    context = {
        'tvShowsList': tvShowsList
    }
    template = loader.get_template('tvshows/index.html')

    return HttpResponse(template.render(context,request))


def details(request, tvShowId):
    tvShow = get_object_or_404(TvShow, id=tvShowId)
    
    context = {
        'tvShow': tvShow
    }
    template = loader.get_template('tvshows/details.html')

    return HttpResponse(template.render(context,request))