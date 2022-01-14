"""
WSGI config for proj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'samsr.settings')
#
# application = get_wsgi_application()


import os

from django.core.wsgi import get_wsgi_application

print(
    "environment value for DJANGO_SETTINGS_ENVIRONMENT  -- > ",
    os.getenv("DJANGO_SETTINGS_ENVIRONMENT"),
)
environment = os.getenv("DJANGO_SETTINGS_ENVIRONMENT")

# if environment == "development":
#     print("Loading development settings file for Django configurations")
#     os.environ["DJANGO_SETTINGS_MODULE"] = "rummyplatform.settings.dev"
# elif environment == "production":
#     print("Loading production settings file for Django configurations")
#     os.environ["DJANGO_SETTINGS_MODULE"] = "rummyplatform.settings.prod"
# else:
#     print("Loading local settings file for Django configurations")
#     os.environ["DJANGO_SETTINGS_MODULE"] = "rummyplatform.settings.local"

print(os.getenv("DJANGO_SETTINGS_MODULE"))
application = get_wsgi_application()

