from django.db import models
from aircraft.models import AirCraft

# Create your models here.

class Flight(models.Model):
    """
    Flight models related info
    """
    msn = models.CharField(max_length=500, unique=True)
    flight_aircraft = models.ForeignKey(AirCraft, on_delete=models.CASCADE)
    fuel_quantity_left_wing = models.IntegerField()
    fuel_quantity_right_wing = models.IntegerField()
    maximum_altitude = models.IntegerField()
