from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import TvShow, Episode, Season
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


class EpisodeCreate(CreateView):
    model = Episode
    fields = ['season', 'number', 'title', 'description', 'videoUrl', 'duration', 'releaseDate']

    def get_success_url(self):
        tvshow = self.object.season.tvShow
        return reverse_lazy('tvshows:details', kwargs={'tvShowId': tvshow.id})


class EpisodeUpdate(UpdateView):
    model = Episode
    fields = ['season', 'number', 'title', 'description', 'videoUrl', 'duration', 'releaseDate']

    def get_success_url(self):
        tvshow = self.object.season.tvShow
        return reverse_lazy('tvshows:details', kwargs={'tvShowId': tvshow.id})


class EpisodeDelete(DeleteView):
    model = Episode

    def get_success_url(self):
        tvshow = self.object.season.tvShow
        return reverse_lazy('tvshows:details', kwargs={'tvShowId': tvshow.id})

class SeasonCreate(CreateView):
    model = Season
    fields = ['tvShow', 'number']

    def get_success_url(self):
        tvshow = self.object.tvShow
        return reverse_lazy('tvshows:details', kwargs={'tvShowId': tvshow.id})


class SeasonUpdate(UpdateView):
    model = Season
    fields = ['number']

    def get_success_url(self):
        tvshow = self.object.tvShow
        return reverse_lazy('tvshows:details', kwargs={'tvShowId': tvshow.id})


class SeasonDelete(DeleteView):
    model = Season

    def get_success_url(self):
        tvshow = self.object.tvShow
        return reverse_lazy('tvshows:details', kwargs={'tvShowId': tvshow.id})
