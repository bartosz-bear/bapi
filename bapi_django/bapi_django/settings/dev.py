from decouple import config

DEBUG = True
ALLOWED_HOSTS = [config('HOST')]