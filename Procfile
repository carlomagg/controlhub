web: python manage.py migrate && python manage.py create_superuser_if_none && python manage.py collectstatic --noinput && daphne -b 0.0.0.0 -p $PORT controlhub.asgi:application
