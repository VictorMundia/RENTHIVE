from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import MaintenanceTicket
from .serializers import MaintenanceTicketSerializer

# Create your views here.

class MaintenanceTicketViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceTicket.objects.all()
    serializer_class = MaintenanceTicketSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'priority', 'assigned_to', 'unit']
    search_fields = ['title', 'description']
