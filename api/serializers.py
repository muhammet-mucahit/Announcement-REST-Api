from rest_framework import serializers
from .models import Panel

class PanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panel
        fields = ('icon', 'title', 'created',)