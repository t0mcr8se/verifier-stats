#!/bin/sh

echo "Collect static files"
python manage.py collectstatic --noinput
python manage.py makemigrations

echo "Apply database migrations"
python manage.py migrate

python manage.py createsuperuser --noinput --username admin --email admin@example.com 2> /dev/null

echo "Waiting for postgres..."

while ! nc -z db 5432; do
    sleep 0.1
done

echo "PostgreSQL started"

exec "$@"