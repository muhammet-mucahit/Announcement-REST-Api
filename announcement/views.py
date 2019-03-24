from rest_framework import generics
from .models import Main
from .serializers import MainSerializer
from django.shortcuts import render

# Create your views here.

class ListSongView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Main.objects.all()
    serializer_class = MainSerializer


class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides a get method handler.
    """
    queryset = Main.objects.all()
    serializer_class = MainSerializer

def screen(request):
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'screen.html', {})
 		