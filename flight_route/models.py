from django.db import models
from airport.models import Airport
from flight.models import Flight

# Create your models here.

class FlightRoute(models.Model):
    """
    Model for flight route info
    """
    start_location = models.ForeignKey(Airport, related_name="departed_from", on_delete=models.CASCADE)
    end_location = models.ForeignKey(Airport, related_name="arrived_at", on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    flight_number = models.CharField(max_length=50)


class JourneyInfo(models.Model):
    """
    model for journeyinfo
    """
    flight_route = models.ForeignKey(FlightRoute, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    journey_date = models.DateField()
