from .base import *

DEBUG = False

ADMINS = (
    ('Monkey', 'Monkey@mydomain.com'),
)


ALLOWED_HOSTS = ['*']


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

# Security

CSRF_TRUSTED_ORIGINS = ['https://127.0.0.1',
                        'https://eduproject.com',
                        'https://www.eduproject.com']
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
