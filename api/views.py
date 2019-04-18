# from django.shortcuts import render
from rest_framework import generics
from .models import Panel
from .serializers import PanelSerializer

# Create your views here.

class PanelList(generics.ListAPIView):
    queryset = Panel.objects.all()
    serializer_class = PanelSerializer

class PanelDetail(generics.RetrieveAPIView):
    queryset = Panel.objects.all()
    serializer_class = PanelSerializer