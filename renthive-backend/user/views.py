from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['role', 'is_active']
    search_fields = ['email', 'first_name', 'last_name']
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    # Optionally, restrict some actions to admins only
    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update', 'create']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
