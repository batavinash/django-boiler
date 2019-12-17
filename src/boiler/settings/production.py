from .base import *

DEBUG = False

ALLOWED_HOSTS = ["ip-address", "www.example.com"]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": 'your-db-name',
        'USER': 'your-user-name',
        'PASSWORD': 'your db password',
        'HOST': 'localhost',
        'PORT': ''
    }
}