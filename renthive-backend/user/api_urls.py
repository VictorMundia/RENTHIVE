from django.urls import path
from .api_views import RegisterAPIView

urlpatterns = [
    path('api/register/', RegisterAPIView.as_view(), name='api_register'),
]
