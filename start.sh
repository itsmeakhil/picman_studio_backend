#!/bin/bash

echo "Starting Picman API Django application"
export DJANGO_SETTINGS_MODULE="picman_studio_backend.settings"
gunicorn --workers=3 --bind=0.0.0.0:8000 picman_studio_backend.wsgi:application  --threads=3 --worker-connections=500 --log-level=debug --timeout=120