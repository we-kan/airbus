from django.db import models

# Create your models here.

class AirCraft(models.Model):
    """
    Aircraft models related info
    """
    name = models.CharField(max_length=1000)
    fuel_capacity_right_wing = models.IntegerField()
    fuel_capacity_left_wing = models.IntegerField()
    gross_weight = models.IntegerField()
    atmospheric_pressure = models.IntegerField()
    room_temperature = models.IntegerField()
