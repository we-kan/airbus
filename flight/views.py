from rest_framework import status, viewsets

from flight.models import Flight
from flight.serializers import FlightSerializer

# Create your views here.
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
