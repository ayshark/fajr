from rest_framework import serializers
from .models import Tracker


class TrackerSerializer(serialzers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = ['date', 'daily_status']