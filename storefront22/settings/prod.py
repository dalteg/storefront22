import os
import dj_database_url
from .common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
    )
}

# Redis
REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

CELERY_BROKER_URL = REDIS_URL + '/1'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL + '/2',
        "TIMEOUT": 10 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SILKY_PYTHON_PROFILER = False

# Disable debug-only apps in production
INSTALLED_APPS = [app for app in INSTALLED_APPS if app not in [
    'debug_toolbar',
    'silk',
]]

MIDDLEWARE = [m for m in MIDDLEWARE if m not in [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'silk.middleware.SilkyMiddleware',
]]