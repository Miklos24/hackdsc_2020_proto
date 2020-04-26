from django.shortcuts import render

from rest_framework import viewsets

from .serializers import HostSerializer, EventSerializer
from .models import Host, Event

# Create your views here.
class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all().order_by('name')
    serializer_class = HostSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('name')
    serializer_class = EventSerializer
