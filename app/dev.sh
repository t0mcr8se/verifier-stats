#!/bin/sh

pip install -r /workspace/app/requirements.txt
python /workspace/app/manage.py migrate
python /workspace/app/manage.py createsuperuser --noinput --username admin --email admin@example.com 2>/dev/null