#!/bin/bash

# Run migrations
python manage.py migrate --noinput

# Create superuser if none exists
python manage.py create_superuser_if_none

# Collect static files
python manage.py collectstatic --noinput

# Start the application with Daphne (ASGI server for Django Channels)
daphne -b 0.0.0.0 -p ${PORT:-8000} controlhub.asgi:application
