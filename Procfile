release: python manage.py migrate
web: gunicorn storefront22.wsgi:application
worker: celery -A storefront22 worker

