from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tvshows/', include('tvshows.urls')),
    path('restapi/tvshows/', views.TvShowList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)