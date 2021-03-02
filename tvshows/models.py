from django.db import models
from django.urls import reverse

class TvShow(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    poster = models.CharField(max_length=1000)
    description = models.CharField(max_length=2500)
    productionCountry = models.CharField(max_length=40)

    def get_absolute_url(self):
        return reverse('tvshows:details', kwargs={'tvShowId': self.id})

    def __str__(self):
        return "[" + str(self.id) + "] " + self.title + " (" + self.productionCountry + ") - " + self.genre + "\n" + self.description[0:100] + "(...)"


class Season(models.Model):
    tvShow = models.ForeignKey(TvShow, on_delete=models.CASCADE)
    number = models.SmallIntegerField()

    def get_success_url(self):
        return reverse('tvshows:details', kwargs={'tvShowId': self.tvShow.id})

    def get_absolute_url(self):
        return reverse('tvshows:details', kwargs={'tvShowId': self.tvShow.id})

    def __str__(self):
        return self.tvShow.title + " - season " + str(self.number)


class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    number = models.SmallIntegerField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2500)
    duration = models.DurationField()
    releaseDate = models.DateField()
    videoUrl = models.CharField(max_length=2500)

    def get_success_url(self):
        return reverse('tvshows:details', kwargs={'tvShowId': self.season.tvShow.id})

    def get_absolute_url(self):
        return reverse('tvshows:details', kwargs={'tvShowId': self.season.tvShow.id})

    def __str__(self):
        return self.season.tvShow.title + " [S" + str(self.season.number) + "E" + str(self.number) + "] [duration: " + str(self.duration) + "] released: " + str(self.releaseDate)
