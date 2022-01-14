import os
from .base import *
DEBUG = True
print("In local settings")
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'rehman',
        'HOST': 'localhost',
        'PORT': '5432'
    },
    'task_db': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'task_db',
        'USER': 'postgres',
        'PASSWORD': 'rehman',
        'HOST': 'localhost',
        'PORT': '5432'
    },
}