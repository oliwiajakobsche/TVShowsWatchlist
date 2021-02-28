from django.urls import path, include
from . import views

app_name = 'tvshows'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:tvShowId>', views.details, name='details')
]
