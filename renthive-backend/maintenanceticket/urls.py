from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MaintenanceTicketViewSet

router = DefaultRouter()
router.register(r'maintenanceticket', MaintenanceTicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
