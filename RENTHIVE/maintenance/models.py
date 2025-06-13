from django.db import models

# Create your models here.
class MaintenanceRequest(models.Model):
    tenant = models.ForeignKey('tenants.Tenant', on_delete=models.CASCADE)
    unit = models.ForeignKey('units.Unit', on_delete=models.CASCADE)
    issue_type = models.CharField(max_length=100)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    vacancy_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Issue: {self.issue_type} - Unit: {self.unit}"
