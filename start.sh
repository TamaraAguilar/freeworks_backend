#!/bin/bash
echo "Ejecutando migraciones de base de datos..."
python manage.py migrate

echo "Iniciando servidor Gunicorn..."
gunicorn freeworks_backend.wsgi:application --bind 0.0.0.0:8000