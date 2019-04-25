from rest_framework import generics
from .models import Panel
from .serializers import PanelSerializer

class PanelList(generics.ListAPIView):
    queryset = Panel.objects.all()
    serializer_class = PanelSerializer

class PanelDetail(generics.RetrieveAPIView):
    queryset = Panel.objects.all()
    serializer_class = PanelSerializer