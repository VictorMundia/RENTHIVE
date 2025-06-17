from django.db import models

# Create your models here.
from django.db import models
from user.models import User

class Message(models.Model):
    CHANNEL_CHOICES = [
        ('APP', 'In-App'),
        ('SMS', 'SMS'),
        ('EMAIL', 'Email'),
    ]
    
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=100)
    body = models.TextField()
    channel = models.CharField(max_length=10, choices=CHANNEL_CHOICES, default='APP')
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to='message_attachments/', null=True, blank=True)

    def __str__(self):
        return f"{self.subject} ({self.channel})"