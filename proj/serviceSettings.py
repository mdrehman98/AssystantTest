from django.urls import path, include
import sys
import logging

logger = logging.getLogger(__name__)
print(logger)


def getServiceSettings(SERVICE_APPS):
    SERVICE_CONFIGURATIONS = {
        "SERVICE_NAME": '',
        "INSTALLED_APPS": [],
        "DB_ROUTERS": []
    }

    SERVICE_NAME = ''
    print(sys.argv)
    set1 = set(sys.argv)
    set2 = set(SERVICE_APPS)
    servicename = set1.intersection(set2)

    print('servicename from intersection - ', servicename)
    if servicename and len(servicename) > 0:
        SERVICE_NAME = list(servicename)[0]
    print('SERVICE_NAME - ', SERVICE_NAME)

    if SERVICE_NAME == 'taskapp':
        SERVICE_CONFIGURATIONS = {
            "SERVICE_NAME": 'taskapp',
            "INSTALLED_APPS": ['taskapp'],
            "DB_ROUTERS": ['taskapp.config.dbRouter.UserRouter'],
        }

    elif 'manage.py' in set1 or '.\\manage.py' in set1 or 'runserver' in set1:
        SERVICE_CONFIGURATIONS = {
            "SERVICE_NAME": 'allservice',
            "INSTALLED_APPS": SERVICE_APPS,
            "DB_ROUTERS": [
                'taskapp.config.dbRouter.UserRouter']
        }
    else:
        SERVICE_CONFIGURATIONS = {
            "SERVICE_NAME": 'defaultservice',
            "INSTALLED_APPS": SERVICE_APPS,
            "DB_ROUTERS": [
                          'taskapp.config.dbRouter.UserRouter']
        }
    return SERVICE_CONFIGURATIONS