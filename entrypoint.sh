#!/bin/sh

echo ">>> Aplicando migraciones..."
python manage.py migrate --noinput

echo ">>> Iniciando Gunicorn..."
exec gunicorn configuracion.wsgi:application --bind 0.0.0.0:8000 --workers 3
