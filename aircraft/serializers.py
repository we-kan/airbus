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
        fields = '__all__'
