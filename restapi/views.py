from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tvshows.models import TvShow, Season, Episode
from restapi.serializers import TvShowSerializer

class TvShowList(APIView):

    def get(self, request):
        tvShows = TvShow.objects.all()
        serializer = TvShowSerializer(tvShows, many=True)
        return Response(serializer.data)