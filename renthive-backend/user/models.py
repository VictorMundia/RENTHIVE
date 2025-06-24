from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('TENANT', 'Tenant'),
        ('OWNER', 'Property Owner'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, unique=True)
    national_id = models.CharField(max_length=20, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
