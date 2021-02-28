from django.contrib import admin
from .models import TvShow, Season, Episode

admin.site.register(TvShow)
admin.site.register(Season)
admin.site.register(Episode)