#!/usr/bin/env python
"""Quick script to check and fix user role"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'controlhub.settings')
django.setup()

from accounts.models import User

username = 'carlomagg'

try:
    user = User.objects.get(username=username)
    print(f"Username: {user.username}")
    print(f"Email: {user.email}")
    print(f"Current Role: {user.role}")
    print(f"Role Display: {user.get_role_display()}")
    print(f"Is Superuser: {user.is_superuser}")
    print(f"Is Staff: {user.is_staff}")
    print(f"Can send messages: {user.can_send_messages()}")
    print(f"Can manage users: {user.can_manage_users()}")
    print(f"Can monitor devices: {user.can_monitor_devices()}")
    
    if user.role != 'super_admin':
        print("\n⚠️ Role is not super_admin! Fixing...")
        user.role = 'super_admin'
        user.save()
        print("✅ Role updated to super_admin")
    else:
        print("\n✅ Role is correct!")
        
except User.DoesNotExist:
    print(f"❌ User '{username}' not found!")
