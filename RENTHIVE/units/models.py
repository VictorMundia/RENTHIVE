from django.db import models

# Create your models here.
class Unit(models.Model):
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=20)
    type = models.CharField(max_length=50)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    vacancy_status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.unit_number} - {self.property}"
