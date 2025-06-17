from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyTypeViewSet

router = DefaultRouter()
router.register(r'propertytypes', PropertyTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
