from config.settings.base import *

SECRET_KEY = 'g)xal-du=ftd&8fuv%yw8tnq9og7m=2lkllptv2kv4tbl29wi)'

DEBUG = False

ADMINS = [('Adarsh S', '4darshofficial@gmail.com'),]

ALLOWED_HOSTS = []

CORS_ORIGIN_WHITELIST = [
]

CORS_ORIGIN_REGEX_WHITELIST = (
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
        'throttles.BurstRateThrottle',
        'throttles.SustainedRateThrottle'),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/day',
        'user': '200/day',
        'burst': '10/min',
        'sustained': '20/day'
    }
}
