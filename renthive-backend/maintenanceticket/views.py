from django.shortcuts import render
from rest_framework import viewsets
from .models import MaintenanceTicket
from .serializers import MaintenanceTicketSerializer

# Create your views here.

class MaintenanceTicketViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceTicket.objects.all()
    serializer_class = MaintenanceTicketSerializer
