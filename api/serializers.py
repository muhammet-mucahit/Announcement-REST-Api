from rest_framework import serializers
from .models import Panel, SlidingText

class SlidingTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlidingText
        fields = ('text',)

class PanelSerializer(serializers.ModelSerializer):
    # tracks = serializers.StringRelatedField(many=True)
    # sliding_texts = serializers.StringRelatedField(read_only=True, many=True)
    # sliding_texts = serializers.SlugRelatedField(many=True, read_only=True, slug_field='text')
    sliding_texts = SlidingTextSerializer(many=True)

    class Meta:
        model = Panel
        fields = ('icon', 'title', 'created', 'sliding_texts',)
