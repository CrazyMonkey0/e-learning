from .base import *

DEBUG = False

ADMINS = (
    ('Monkey', 'Monkey@mydomain.com'),
)


ALLOWED_HOSTS = ['*', 'eduproject.com', 'www.eduproject.com']


DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
