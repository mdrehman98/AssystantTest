"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
]

print(urlpatterns)
SERVICE_CONFIGURATIONS = settings.SERVICE_CONFIGURATIONS
SERVICE_NAME = ''
if SERVICE_CONFIGURATIONS and SERVICE_CONFIGURATIONS.get('SERVICE_NAME', ''):
    SERVICE_NAME = SERVICE_CONFIGURATIONS.get('SERVICE_NAME', '')

if SERVICE_NAME == 'taskapp':
    urlpatterns += [path('taskService/', include('taskapp.urls')), ]

#elif SERVICE_NAME == 'backofficeservice':
#    urlpatterns += [path('backOffice/', include('backofficeservice.urls')), ]
elif SERVICE_NAME in ['allservice']:
    urlpatterns += [
        path('taskService/', include('taskapp.urls')),
#        path('backOffice/', include('backofficeservice.urls')),
    ]