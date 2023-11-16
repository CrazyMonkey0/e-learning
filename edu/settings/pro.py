from .base import *

DEBUG = True

ADMINS = (
    ('Monkey', 'Monkey@mydomain.com'),
)

# ALLOWED_HOSTS = ['eduproject.com', 'www.eduproject.com']
ALLOWED_HOSTS = ['*']


#
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
