from django.db import models

# Create your models here.
from django.db import models
from leases.models import Lease
from user.models import User

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('MPESA', 'M-Pesa'),
        ('CASH', 'Cash'),
        ('BANK', 'Bank Transfer'),
    ]
    
    lease = models.ForeignKey(Lease, on_delete=models.PROTECT, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    transaction_code = models.CharField(max_length=50, unique=True)
    is_confirmed = models.BooleanField(default=False)
    confirmed_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Payment {self.transaction_code}"