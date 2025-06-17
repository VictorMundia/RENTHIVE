from django.db import models

from django.db import models
from user.models import User
from propertytype.models import PropertyType

class Property(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties', limit_choices_to={'role': 'OWNER'})
    property_type = models.ForeignKey(PropertyType, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    location = models.JSONField()  # {county: "", coordinates: {lat, lng}}
    amenities = models.JSONField(default=list)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.property_type.name}"