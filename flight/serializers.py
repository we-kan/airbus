from rest_framework import serializers

from flight.models import Flight

class FlightSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Flight
