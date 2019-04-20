from rest_framework import serializers
from .models import Panel, SlidingText

class SlidingTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlidingText
        fields = ('text',)

class PanelSerializer(serializers.ModelSerializer):
    sliding_texts = SlidingTextSerializer(many=True)

    class Meta:
        model = Panel
        fields = ('icon', 'title', 'created', 'video', 'sliding_texts',)
