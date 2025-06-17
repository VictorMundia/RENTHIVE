from django.db import models

# Create your models here.
from django.db import models
from payments.models import Payment
from django.utils import timezone

class Receipt(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, related_name='receipt')
    receipt_number = models.CharField(max_length=20, unique=True)
    issued_at = models.DateTimeField(auto_now_add=True)
    download_url = models.URLField(blank=True)
    digital_signature = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.receipt_number:
            self.receipt_number = f"RCP-{self.payment.id}-{timezone.now().strftime('%Y%m%d')}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.receipt_number