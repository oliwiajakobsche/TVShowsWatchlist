from django.urls import path
from . import views

app_name = 'tvshows'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:tvShowId>', views.details, name='details'),
    path('serie/add', views.TvshowCreate.as_view(), name='tvshow-add'),
    path('<int:pk>/delete', views.TvshowDelete.as_view(), name='tvshow-delete'),
    path('<int:pk>/update', views.TvshowUpdate.as_view(), name='tvshow-update'),
    path('episodes/add', views.EpisodeCreate.as_view(), name='episode-add'),
    path('episodes/<int:pk>/update', views.EpisodeDelete.as_view(), name='episode-delete'),
    path('episodes/<int:pk>/delete', views.EpisodeUpdate.as_view(), name='episode-update'),
    path('seasons/add', views.SeasonCreate.as_view(), name='season-add'),
    path('seasons/<int:pk>/update', views.SeasonDelete.as_view(), name='season-delete'),
    path('seasons/<int:pk>/delete', views.SeasonUpdate.as_view(), name='season-update'),
]