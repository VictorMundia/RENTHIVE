from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
from user.models import User
from unit.models import Unit
from .tasks import send_notification

class MaintenanceTicket(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]
    
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('ASSIGNED', 'Assigned'),
        ('COMPLETED', 'Completed'),
    ]
    
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_tickets', limit_choices_to={'role': 'TENANT'})
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='tickets')
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='MEDIUM')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='OPEN')
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets', limit_choices_to={'role': 'STAFF'})
    _original_status = None

    def __str__(self):
        return f"Ticket #{self.id} - {self.title}"

    def save(self, *args, **kwargs):
        if self.pk:
            orig = MaintenanceTicket.objects.get(pk=self.pk)
            self._original_status = orig.status
        else:
            self._original_status = self.status
        super().save(*args, **kwargs)

    def status_changed(self):
        return self._original_status is not None and self.status != self._original_status

@receiver(post_save, sender=MaintenanceTicket)
def notify_status_change(sender, instance, **kwargs):
    if instance.status_changed():
        send_notification.delay(instance.id, instance._original_status, instance.status)