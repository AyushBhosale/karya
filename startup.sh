#!/bin/bash
# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate --noinput

# Start Gunicorn process
gunicorn karya.wsgi:application --bind=0.0.0.0:8000
