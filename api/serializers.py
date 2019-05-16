from rest_framework import serializers
from .models import Panel, SlidingText, Activity, Class

class SlidingTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlidingText
        fields = ('text',)

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('title', 'owner', 'date', 'address',)

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('title', 'owner', 'day', 'start_time', 'end_time', 'address')

class PanelSerializer(serializers.ModelSerializer):
    sliding_texts = SlidingTextSerializer(many=True)
    activities = ActivitySerializer(many=True)
    classes = ClassSerializer(many=True)

    class Meta:
        model = Panel
        fields = ('icon', 'title', 'video', 'sliding_texts',
                  'activities', 'classes', 'weather_city',)
