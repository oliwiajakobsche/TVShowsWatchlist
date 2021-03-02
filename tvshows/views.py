from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import TvShow
from django.urls import reverse_lazy


def index(request):
    tvShowsList = TvShow.objects.all()
    context = {'tvShowsList': tvShowsList}

    return render(request, 'tvshows/index.html', context)


def details(request, tvShowId):
    tvShow = get_object_or_404(TvShow, id=tvShowId)
    context = {'tvShow': tvShow}

    return render(request, 'tvshows/details.html', context)


class TvshowCreate(CreateView):
    model = TvShow
    fields = ['title', 'genre', 'poster', 'description', 'productionCountry']


class TvshowUpdate(UpdateView):
    model = TvShow
    fields = ['title', 'genre', 'poster', 'description', 'productionCountry']


class TvshowDelete(DeleteView):
    model = TvShow
    success_url = reverse_lazy('tvshows:index')
