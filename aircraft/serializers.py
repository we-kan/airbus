from rest_framework import serializers

from .models import AirCraft, AirCraftInfo

class AircraftSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = AirCraft
        fields = '__all__'


class AircraftInfoSerializer(serializers.ModelSerializer):
    """

    """
    aircraft = AircraftSerializer()

    class Meta:
        model = AirCraftInfo
        fields = ('aircraft', 'fuel_capacity_right_wing', 'fuel_capacity_left_wing', 'gross_weight', 'harness_length', 'atmospheric_pressure', 'room_temperature')
