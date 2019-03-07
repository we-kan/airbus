from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import AircraftSerializer, AircraftInfoSerializer
from search.serializers import DataSerializer
from .models import AirCraftInfo, AirCraft

class AircraftView(ModelViewSet):
    """

    """
    queryset = AirCraft.objects.all()
    serializer_class = AircraftSerializer


class AircraftInfoView(ModelViewSet):
    """

    """
    queryset = AirCraftInfo.objects.all()
    serializer_class = DataSerializer
