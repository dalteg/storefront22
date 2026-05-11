release: python manage.py migrate
web: gunicorn storefront22.wsgi --workers 2 --threads 2
worker: celery -A storefront22 worker