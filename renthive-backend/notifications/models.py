from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from user.models import User
from django.contrib.contenttypes.models import ContentType

class Notification(models.Model):
    """
    System-wide notifications for users
    """
    NOTIFICATION_TYPES = (
        ('PAYMENT_RECEIVED', 'Payment Received'),
        ('PAYMENT_REMINDER', 'Payment Reminder'),
        ('MAINTENANCE_UPDATE', 'Maintenance Update'),
        ('LEASE_RENEWAL', 'Lease Renewal'),
        ('SYSTEM_ALERT', 'System Alert'),
    )
    
    PRIORITY_LEVELS = (
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('URGENT', 'Urgent'),
    )

    # Recipient information
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    
    # Notification content
    notification_type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES
    )
    title = models.CharField(max_length=100)
    message = models.TextField()
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_LEVELS,
        default='MEDIUM'
    )
    
    # Status tracking
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    
    # Actionable content
    action_url = models.URLField(blank=True, null=True)
    action_text = models.CharField(max_length=30, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    
    # Reference to related objects (generic approach)
    content_type = models.ForeignKey(
        'contenttypes.ContentType',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'is_read']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.notification_type} - {self.user.username}"

    def mark_as_read(self):
        if not self.is_read:
            self.is_read = True
            self.read_at = timezone.now()
            self.save()

    @property
    def days_old(self):
        return (timezone.now() - self.created_at).days

    @classmethod
    def create_payment_notification(cls, user, payment):
        return cls.objects.create(
            user=user,
            notification_type='PAYMENT_RECEIVED',
            title=f"Payment Confirmed - KSh {payment.amount}",
            message=f"Your payment for {payment.lease.unit} has been processed.",
            action_url=f"/payments/{payment.id}",
            action_text="View Receipt",
            content_type=ContentType.objects.get_for_model(payment),
            object_id=payment.id
        )