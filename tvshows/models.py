from django.db import models


class TvShow(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    poster = models.CharField(max_length=1000)
    description = models.CharField(max_length=2500)
    productionCountry = models.CharField(max_length=40)

    def __str__(self):
        return "[" + str(self.id) + "] " + self.title + " (" + self.productionCountry + ") - " + self.genre + "-" + self.description[0:100]


class Season(models.Model):
    tvShow = models.ForeignKey(TvShow, on_delete=models.CASCADE)
    number = models.SmallIntegerField()

    def __str__(self):
        return self.tvShow.title + " - season " + str(self.number)


class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    number = models.SmallIntegerField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2500)
    duration = models.DurationField()
    releaseDate = models.DateField()

    def __str__(self):        
        return self.season.tvShow.title + " [S" + str(self.season.number) + "E" + str(self.number) + "] [duration: " + str(self.duration) + "] released: " + str(self.releaseDate)
