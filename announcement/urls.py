from django.urls import path
from .views import ListSongView, SongDetailView, screen


urlpatterns = [
	path('', screen, name='screen'),
    path('songs/', ListSongView.as_view(), name="songs-all"),
    path('songs/<int:pk>/', SongDetailView.as_view(), name="songs-detail"),
]