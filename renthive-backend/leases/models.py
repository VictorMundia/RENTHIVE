from django.db import models

# Create your models here.
from django.db import models
from user.models import User
from unit.models import Unit

class Lease(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='leases')
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leases', limit_choices_to={'role': 'TENANT'})
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    payment_due_day = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    terms = models.TextField(blank=True)

    def __str__(self):
        return f"Lease #{self.id} - {self.unit}"