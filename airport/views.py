from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import AirportSerializer
from .models import Airport
# Create your views here.

class AirportInfoView(ModelViewSet):
    """

    """
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
