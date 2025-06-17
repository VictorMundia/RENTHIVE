from django.db import models

# Create your models here.
from django.db import models
from properties.models import Property
from user.models import User

class Unit(models.Model):
    STATUS_CHOICES = [
        ('VACANT', 'Vacant'),
        ('OCCUPIED', 'Occupied'),
        ('MAINTENANCE', 'Under Maintenance'),
    ]
    
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='units')
    unit_number = models.CharField(max_length=20)
    bedrooms = models.PositiveSmallIntegerField(default=1)
    bathrooms = models.PositiveSmallIntegerField(default=1)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='VACANT')
    current_tenant = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, limit_choices_to={'role': 'TENANT'})

    def __str__(self):
        return f"{self.property.name} - Unit {self.unit_number}"