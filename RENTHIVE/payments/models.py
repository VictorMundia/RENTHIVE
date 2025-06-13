from django.db import models

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_code = models.CharField(max_length=100)
    payment_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.transaction_code} - {self.amount}"
