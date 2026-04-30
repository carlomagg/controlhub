from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ('super_admin', 'Super Admin'),
        ('admin', 'Admin'),
        ('viewer', 'Viewer'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    def is_super_admin(self):
        return self.role == 'super_admin'
    
    def is_admin(self):
        return self.role in ['super_admin', 'admin']
    
    def can_manage_users(self):
        return self.role in ['super_admin', 'admin']
    
    def can_monitor_devices(self):
        return self.role in ['super_admin', 'admin']
    
    def can_send_messages(self):
        return self.role in ['super_admin', 'admin']
