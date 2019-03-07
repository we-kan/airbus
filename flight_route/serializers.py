from rest_framework import serializers

from flight_route.models import FlightRoute, JourneyInfo 

class FlightRouteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FlightRoute

class JourneyInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JourneyInfo


