#!/usr/bin/env bash

pip install -r requirements.txt
python manage.py migrate --settings=storefront22.settings.prod
python manage.py loaddata datadump.json --settings=storefront22.settings.prod
python manage.py collectstatic --noinput
