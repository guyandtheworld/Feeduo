from base import *
from decouple import config, Csv
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ADMINS = [('Adarsh S', '4darshofficial@gmail.com'),]

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

CORS_ORIGIN_WHITELIST = [
]

CORS_ORIGIN_REGEX_WHITELIST = (
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
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
