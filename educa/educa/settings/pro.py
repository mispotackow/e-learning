from .base import *

DEBUG = False

ADMINS = (
    ('Potakov M', 'potackiw@gmail.com'),
)

ALLOWED_HOSTS = ['.educapotackow.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'potackow1'
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
