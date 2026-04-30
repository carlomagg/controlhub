from django.db import models
from django.utils import timezone
import secrets


class Device(models.Model):
    STATUS_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('connecting', 'Connecting'),
    ]
    
    device_name = models.CharField(max_length=255)
    unique_token = models.CharField(max_length=64, unique=True, editable=False)
    operating_system = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='offline')
    last_seen = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Additional metadata
    hostname = models.CharField(max_length=255, blank=True)
    cpu_info = models.CharField(max_length=255, blank=True)
    ram_total = models.CharField(max_length=50, blank=True)
    screen_resolution = models.CharField(max_length=50, blank=True)
    
    class Meta:
        ordering = ['-last_seen']
    
    def __str__(self):
        return f"{self.device_name} ({self.operating_system})"
    
    def save(self, *args, **kwargs):
        if not self.unique_token:
            self.unique_token = secrets.token_urlsafe(48)
        super().save(*args, **kwargs)
    
    def update_last_seen(self):
        self.last_seen = timezone.now()
        self.save(update_fields=['last_seen'])
    
    def set_online(self):
        self.status = 'online'
        self.last_seen = timezone.now()
        self.save(update_fields=['status', 'last_seen'])
    
    def set_offline(self):
        self.status = 'offline'
        self.save(update_fields=['status'])
