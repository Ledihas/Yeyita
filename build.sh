#!/usr/bin/env bash

set -o errexit  # Termina el script si hay un error

# Instala las dependencias
pip install -r requirements.txt

# Reúne archivos estáticos
python manage.py collectstatic --no-input

# Realiza las migraciones de la base de datos
python manage.py migrate
