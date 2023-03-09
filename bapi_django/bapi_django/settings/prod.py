from decouple import config

DEBUG = False
ALLOWED_HOSTS = [config('PRODUCTION_HOST')]
SESION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True