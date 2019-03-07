from django.db import models

# Create your models here.

class AirCraft(models.Model):
    """
    Aircraft name
    """
    name = models.CharField(max_length=1000)

class AirCraftInfo(models.Model):
    """
    Aircraft Info models related info
    """
    aircraft = models.OneToOneField(AirCraft, on_delete=models.CASCADE)
    fuel_capacity_right_wing = models.IntegerField()
    fuel_capacity_left_wing = models.IntegerField()
    gross_weight = models.IntegerField()
    harness_length = models.IntegerField()
    atmospheric_pressure = models.IntegerField()
    room_temperature = models.IntegerField()
