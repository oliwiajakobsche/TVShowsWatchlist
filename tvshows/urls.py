from django.urls import path
from . import views

app_name = 'tvshows'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:tvShowId>', views.details, name='details'),
    path('serie/add', views.TvshowCreate.as_view(), name='tvshow-add'),
    path('<int:pk>/delete', views.TvshowDelete.as_view(), name='tvshow-delete'),
    path('<int:pk>/update', views.TvshowUpdate.as_view(), name='tvshow-update'),
]