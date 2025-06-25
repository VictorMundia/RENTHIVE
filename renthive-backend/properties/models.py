from django.db import models

from django.db import models
from django.conf import settings
from user.models import User
from propertytype.models import PropertyType

class ProofOfOwnership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.FileField(upload_to='ownership_proofs/')
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='Pending Verification')

class Property(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='properties')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    unit_count = models.PositiveIntegerField(default=1)  # <-- Make sure this exists
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)  # <-- And this
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.property_type.name}"