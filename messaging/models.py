from django.db import models
from django.conf import settings
from devices.models import Device


class Message(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Message to {self.device.device_name} from {self.sender.username}"
    
    def mark_delivered(self):
        self.delivered = True
        self.save(update_fields=['delivered'])
    
    def mark_read(self):
        self.read = True
        self.save(update_fields=['read'])
