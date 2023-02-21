from .base import *

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