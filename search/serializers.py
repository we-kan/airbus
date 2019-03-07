from rest_framework import serializers

from airport.serializers import AirportSerializer
from aircraft.serializers import AircraftSerializer, AircraftInfoSerializer
from flight.serializers import FlightSerializer
from flight_route.serializers import FlightRouteSerializer, JourneyInfoSerializer
from aircraft.models import AirCraft, AirCraftInfo
from airport.models import Airport
from flight_route.models import FlightRoute, JourneyInfo
from flight.models import Flight


class DataSerializer(serializers.ModelSerializer):
    """

    """
    flight_route = FlightRouteSerializer()
    flight = FlightSerializer()
    class Meta:
        model = JourneyInfo
        fields = '__all__'
