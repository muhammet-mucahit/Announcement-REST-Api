from rest_framework import serializers
from .models import Panel, SlidingText, Activity

class SlidingTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlidingText
        fields = ('text',)


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('title', 'owner', 'date', 'address',)


class PanelSerializer(serializers.ModelSerializer):
    sliding_texts = SlidingTextSerializer(many=True)
    activities = ActivitySerializer(many=True)

    class Meta:
        model = Panel
        fields = ('icon', 'title', 'video', 'sliding_texts',
                  'activities', 'weather_city',)
