from django.shortcuts import get_object_or_404, render
from .models import TvShow

def index(request):
    tvShowsList = TvShow.objects.all()
    context = { 'tvShowsList': tvShowsList }
    
    return render(request, 'tvshows/index.html', context)


def details(request, tvShowId):
    tvShow = get_object_or_404(TvShow, id=tvShowId)    
    context = { 'tvShow': tvShow }

    return render(request, 'tvshows/details.html', context)