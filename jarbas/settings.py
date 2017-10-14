"""
Django settings for Jarbas project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

from decouple import Csv, config
from dj_database_url import parse

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='my-secret')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())
INTERNAL_IPS = ('127.0.0.1',)


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'test_without_migrations',
    'corsheaders',
    'simple_history',
    'rest_framework',
    'jarbas.core.app.CoreConfig',
    'jarbas.chamber_of_deputies.app.ChamberOfDeputiesConfig',
    'jarbas.api',
    'jarbas.frontend',
    'jarbas.dashboard',
    'django.contrib.admin',
    'django_extensions',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'jarbas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'jarbas.core.context_processors.google_analytics',
            ],
        },
    },
]

WSGI_APPLICATION = 'jarbas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

default_db = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
DATABASES = {
    'default': config('DATABASE_URL', default=default_db, cast=parse)
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'pt_BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
CORE_STATIC_DIR = os.path.join(BASE_DIR, 'jarbas', 'core', 'static')

# Amazon S3 datasets

AMAZON_S3_BUCKET = config('AMAZON_S3_BUCKET', default='serenata-de-amor-data')
AMAZON_S3_REGION = config('AMAZON_S3_REGIN', default='s3-sa-east-1')
AMAZON_S3_CEAPTRANSLATION_DATE = config('AMAZON_S3_CEAPTRANSLATION_DATE', default='2016-08-08')

# Django REST Framework

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'PAGE_SIZE': 7
}

# Google

GOOGLE_ANALYTICS = config('GOOGLE_ANALYTICS', default='')
GOOGLE_STREET_VIEW_API_KEY = config('GOOGLE_STREET_VIEW_API_KEY', default='')


# Twitter

TWITTER_CONSUMER_KEY = config('TWITTER_CONSUMER_KEY', default='')
TWITTER_CONSUMER_SECRET = config('TWITTER_CONSUMER_SECRET', default='')
TWITTER_ACCESS_TOKEN = config('TWITTER_ACCESS_TOKEN', default='')
TWITTER_ACCESS_SECRET = config('TWITTER_ACCESS_SECRET', default='')


# Server headers

USE_X_FORWARDED_HOST = config('USE_X_FORWARDED_HOST', default=False, cast=bool)
SECURE_PROXY_SSL_HEADER = config('SECURE_PROXY_SSL_HEADER', default='', cast=lambda x: tuple(Csv()(x)) or None)

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'


# Cache

default_cache = 'django.core.cache.backends.dummy.DummyCache'
CACHES = {
    'default': {
        'BACKEND': config('CACHE_BACKEND', default=default_cache),
        'LOCATION': config('CACHE_LOCATION', default=None),
        'TIMEOUT': 60 * 60 * 6
    }
}
