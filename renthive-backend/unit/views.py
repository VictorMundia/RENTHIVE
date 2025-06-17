from django.shortcuts import render
from rest_framework import viewsets
from .models import Unit
from .serializers import UnitSerializer

# Create your views here.

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
