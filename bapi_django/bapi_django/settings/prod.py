from decouple import config

DEBUG = False
ALLOWED_HOSTS = [config('PRODUCTION_HOST')]