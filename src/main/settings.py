"""
Django settings for foo project.

Generated by 'django-admin startproject' using Django 1.9.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
from __future__ import unicode_literals

import os

from main import params

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = '/home/zenaida/live/current'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
REPO_ROOT = os.path.dirname(SRC_PATH)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/
DEBUG = getattr(params, 'DEBUG', False)
DEBUGTOOLBAR_ENABLED = False
METRICS_ENABLED = False
CACHE_BACKEND = 'redis_cache.RedisCache'
CACHE_LOCATION = '127.0.0.1:6379'

CACHE_PREFIX = 'zenaida'


# SECURITY WARNING: keep the secret key used in production secret!
# https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-SECRET_KEY

SECRET_KEY = getattr(params, 'SECRET_KEY', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'main.urls'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
    },
    'root': {
        'level': 'DEBUG' if DEBUG else 'WARNING',
        'handlers': ['console', ],
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': [],
        },
    },
    'loggers': {
        'django.request': {
            'level': 'DEBUG',
            'propagate': False,
            'handlers': ['console', ]
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'bootstrap_themes',
    'main',
    'back',
    'front',
    'signup',
]

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'raven.contrib.django.middleware.SentryLogMiddleware',
    # 'raven.contrib.django.middleware.SentryResponseErrorIdMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

# DATABASE DEFAULTS
DATABASES_OPTIONS = {}
DATABASES_TEST = {}
DATABASES_CONN_MAX_AGE = 0

# Sentry defaults
SENTRY_DSN = None

ENV = getattr(params, 'ENV')
STANDALONE = True
if ENV in ['production', 'docker', ]:  # pragma: no cover
    STANDALONE = False


SESSION_COOKIE_NAME = 'zenaida_sid'
CSRF_COOKIE_NAME = 'zenaida_csrftoken'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': getattr(params, 'DATABASES_ENGINE'),
        'NAME': getattr(params, 'DATABASES_NAME'),
        'OPTIONS': DATABASES_OPTIONS,
        'TEST': DATABASES_TEST,
        'CONN_MAX_AGE': DATABASES_CONN_MAX_AGE,
    }
}

# overwrite live settings if something was set in src/main/params.py
for key in ('ENGINE', 'HOST', 'PORT', 'USER', 'PASSWORD'):
    try:
        key_with_prefix = 'DATABASES_{}'.format(key)
        if hasattr(params, key_with_prefix):
            DATABASES['default'][key] = getattr(params, key_with_prefix)
    except KeyError:
        pass


# Caches
CACHES = {
    'default': {
        'BACKEND': CACHE_BACKEND,
        'LOCATION': CACHE_LOCATION,
        'KEY_PREFIX': CACHE_PREFIX
    }
}

# Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
}

LOGIN_REDIRECT_URL = 'index'

# Custom user model
# https://www.codingforentrepreneurs.com/blog/how-to-create-a-custom-django-user-model/
AUTH_USER_MODEL = 'back.Account'

#------------------------------------------------------------------------------

DEFAULT_REGISTRAR_ID = getattr(params, 'DEFAULT_REGISTRAR_ID', 'zenaida_default_registrar')
SUPPORTED_ZONES = getattr(params, 'SUPPORTED_ZONES', ['com', 'net', 'org', ])

