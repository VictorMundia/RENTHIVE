from django.db import models

# Create your models here.
from django.db import models

class PropertyType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=30, blank=True)  # For UI icons

    def __str__(self):
        return self.name