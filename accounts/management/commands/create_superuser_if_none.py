from django.core.management.base import BaseCommand
from accounts.models import User
import os


class Command(BaseCommand):
    help = 'Creates a superuser if none exists'

    def handle(self, *args, **options):
        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
            return

        # Get credentials from environment or use defaults
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@controlhub.com')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            role='admin'
        )

        self.stdout.write(self.style.SUCCESS(f'Superuser created successfully!'))
        self.stdout.write(self.style.SUCCESS(f'Username: {username}'))
        self.stdout.write(self.style.SUCCESS(f'Password: {password}'))
        self.stdout.write(self.style.WARNING('⚠️  IMPORTANT: Change this password after first login!'))
