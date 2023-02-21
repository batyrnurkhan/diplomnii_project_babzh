from .base import *

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = venv("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_PORT = venv("EMAIL_PORT")
EMAIL_HOST_USER = venv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = venv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = "batyrnurhan@gmail.com"
DOMAIN = venv("DOMAIN")
SITE_NAME = "HEES"

DATABASES = {
    'default': {
        'ENGINE': venv('POSTGRES_ENGINE'),
        'NAME': venv('POSTGRES_DB'),
        'USER': venv('POSTGRES_USER'),
        'PASSWORD': venv('POSTGRES_PASSWORD'),
        'HOST': venv('PG_HOST'),
        'PORT': venv('PG_PORT'),
    }
}