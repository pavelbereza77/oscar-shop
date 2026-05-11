#!/bin/sh
# python manage.py migrate
# python manage.py collectstatic --noinput
# exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3 --threads 4


#!/bin/sh
set -e

if [ ! -f manage.py ]; then
    echo ">>> Файл manage.py не найден. Создаем проект Django..."
    django-admin startproject config .
fi

exec "$@"