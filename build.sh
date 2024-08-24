#!/usr/bin/env bash

set -o errexit  # Termina el script si hay un error

# Instala las dependencias
pip install -r requirements.txt

# Reúne archivos estáticos
python manage.py collectstatic

# Realiza las migraciones de la base de datos
python manage.py migrate

# Reinicia la aplicación
touch tmp/restart.txt
