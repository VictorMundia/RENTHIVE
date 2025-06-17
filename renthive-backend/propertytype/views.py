from django.shortcuts import render
from rest_framework import viewsets
from .models import PropertyType
from .serializers import PropertyTypeSerializer

# Create your views here.

class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
