from decouple import config
from .base import *

DEBUG = False
ALLOWED_HOSTS = [config('HOST'), config('HOST_IP'), config('PROD_TEST_HOST'), 'localhost']
SESION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

STATIC_URL = '/static/'
STATIC_ROOT = '/home/bapi/bapi/static'

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["file"]},
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "/var/log/django.log",
            "formatter": "app",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": True
        },
    },
    "formatters": {
        "app": {
            "format": (
                u"%(asctime)s [%(levelname)-8s] "
                "(%(module)s.%(funcName)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
}