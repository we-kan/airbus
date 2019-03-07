from rest_framework import status, viewsets

from flight.models import Flight
from flight_route.models import FlightRoute, JourneyInfo

from flight_route.serializers import FlightRouteSerializer, JourneyInfoSerializer


# Create your views here.
class FlightRouteViewSet(viewsets.ModelViewSet):
    queryset = FlightRoute.objects.all()
    serializer_class = FlightRouteSerializer


class JourneyInfoViewSet(viewsets.ModelViewSet):
    queryset = JourneyInfo.objects.all()
    serializer_class = JourneyInfoSerializer

