from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import News
from .serializers import NewsSerializer
# Create your views here.

class NewsViewSet(ModelViewSet):
    """
    News View
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
