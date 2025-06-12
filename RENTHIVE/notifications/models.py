from django.db import models

class Notification(models.Model):
    tenant = models.ForeignKey('tenants.Tenant', on_delete=models.CASCADE)
    message = models.TextField()
    channel = models.CharField(max_length=50)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To: {self.tenant} - {self.sent_at}"
