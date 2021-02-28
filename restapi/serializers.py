from rest_framework import serializers
from tvshows.models import TvShow, Season, Episode

class TvShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = TvShow
        fields = '__all__'