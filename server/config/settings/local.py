from config.settings.base import *

SECRET_KEY = 'g)xal-du=ftd&8fuv%yw8tnq9og7m=2lkllptv2kv4tbl29wi)'

DEBUG = True

ALLOWED_HOSTS = []


CORS_ORIGIN_WHITELIST = [
    'localhost:8081', 
]

CORS_ORIGIN_REGEX_WHITELIST = (
    'localhost:8081',
)


ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_ann',
        'USER': 'apiadmin',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
        ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '5/day',
        'user': '100/day',
        'burst': '5/min',
        'sustained': '50/day'
    }
}
