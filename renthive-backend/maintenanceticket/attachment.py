from django.db import models
from .models import MaintenanceTicket

class Attachment(models.Model):
    ticket = models.ForeignKey(MaintenanceTicket, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='maintenance_attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment {self.id} for Ticket {self.ticket_id}"
