from .common import *


DEBUG = True

SECRET_KEY = 'django-insecure-^#jui1_5vbjac648#7j(21^k0us9-!^9md#=k&c_ktk(^n*sem'

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront',
        'HOST':'localhost',
        'USER':'root',
        'PASSWORD': '1323'
    }
}