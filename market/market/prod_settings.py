import os
from pathlib import Path

from configuration import *

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = SECRET_DJANGO_KEY

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        'NAME': DB_NAME,
        'USER': LOGIN,
        'PASSWORD': PASS,
        'HOST': HOST,
        'PORT': PORT,
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = []

