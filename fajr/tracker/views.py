from django.shortcuts import render

from rest_framework import viewsets
from .serializer import TrackerSerializer
from .models import Tracker

class TrackerViewSet(viewsets.ModelViewSet):
    queryset = Tracker.objects.all().order_by('date')
    serializer_class = TrackerSerializer
