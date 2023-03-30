from decouple import config
from .base import MIDDLEWARE

DEBUG = False
ALLOWED_HOSTS = [config('HOST'), config('HOST_IP'), config('PROD_TEST_HOST'), 'localhost']
SESION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

STATIC_URL = '/static/'
STATIC_ROOT = '/home/bapi/bapi/static'

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')