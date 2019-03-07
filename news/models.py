from django.db import models

# Create your models here.

class News(models.Model):
    """
    Model for news info
    """
    headline = models.CharField(max_length=1000)
    content = models.TextField()
