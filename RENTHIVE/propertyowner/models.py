from django.db import models
from django.conf import settings

class PropertyOwner(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True  # Makes this a true profile model
    )
    # full_name can be derived from user.get_full_name() or user.first_name and user.last_name
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True) # Phone specific to the owner profile
    # email is already part of settings.AUTH_USER_MODEL (user.email)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username
