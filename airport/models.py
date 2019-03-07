from django.db import models

# Create your models here.
class Airport(models.Model):
    """
    Airport models related info
    """
    airport_code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

