release: python manage.py migrate
web: gunicorn storefront22.wsgi
worker: celery -A storefront22 worker