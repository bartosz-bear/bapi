import os

from .base import *
# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
if os.environ['BAPI_DJANGO_ENV'] == 'prod':
   from .prod import *
else:
   from .dev import *