#!/usr/bin/env bash
set -e

pip install -r requirements.txt
python manage.py migrate --settings=storefront22.settings.prod
python manage.py seed_db --settings=storefront22.settings.prod
python manage.py collectstatic --noinput

python manage.py createsuperuser --noinput --username admin --email admin@admin.com --settings=storefront22.settings.prod
