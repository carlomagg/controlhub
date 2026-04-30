"""
Management command to create a default superuser if none exists.
This is useful for initial deployment.
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()


class Command(BaseCommand):
    help = 'Creates a default superuser if no users exist'

    def handle(self, *args, **options):
        # Check if any users exist
        if User.objects.exists():
            self.stdout.write(
                self.style.WARNING('Users already exist. Skipping superuser creation.')
            )
            return

        # Get credentials from environment variables or use defaults
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@controlhub.com')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')

        try:
            # Create superuser
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
                role='admin'
            )
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created superuser: {username}')
            )
            self.stdout.write(
                self.style.SUCCESS(f'Email: {email}')
            )
            self.stdout.write(
                self.style.WARNING(f'Password: {password}')
            )
            self.stdout.write(
                self.style.WARNING('⚠️  IMPORTANT: Change this password after first login!')
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating superuser: {str(e)}')
            )
