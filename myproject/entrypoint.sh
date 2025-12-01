#!/bin/bash

# Exit on error
set -e
cd /app/api
# Apply database migrations


# Collect static files (optional)
# echo "Collecting static files..."
# python manage.py collectstatic --noinput

# Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000