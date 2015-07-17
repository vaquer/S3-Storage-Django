"""
Django settings for s3Storage project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# IMPORT SETTINGS TO AWS AND DATABASE
conf = None
with open(os.path.join(BASE_DIR, 'conf.json'), 'r') as json_file:
    conf = json.load(json_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bc1wxcubuj3_*=h9&ykx55mxa@xrd^rd+-mb4&8*(s#_)s81dl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    's3Storage',
    'compressor',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 's3Storage.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 's3Storage/templates')],
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

WSGI_APPLICATION = 's3Storage.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': conf['database']['name'],
        'USER': conf['database']['user'],
        'PASSWORD': conf['database']['password'],
        # 'HOST': 'localhost'
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# AWS CONFIGURATIONS
AWS_STORAGE_BUCKET_NAME = 'static-django-meet'
AWS_STORAGE_BUCKET_NAME_MEDIA = 'media-django-meet'
AWS_ACCESS_KEY_ID = conf['aws']['acces_key']
AWS_SECRET_ACCESS_KEY = conf['aws']['secret_key']
AWS_S3_CUSTOM_DOMAIN = '{0}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)
AWS_S3_CUSTOM_DOMAIN_MEDIA = '{0}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME_MEDIA)


# STATIC CONFIGS
STATIC_URL = '/static/'
# STATIC_URL = 'https://{0}/'.format(AWS_S3_CUSTOM_DOMAIN)
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# SET THIS FEATURES ONLY WITH DJANGO COMPRESSOR
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',)
# STATICFILES_STORAGE = 's3Storage.custom_storages.CustomStaticStorage'


# COMPRESSOR SETTINGS
COMPRESS_ENABLED = False
COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = os.path.join(BASE_DIR, 'static')
COMPRESS_STORAGE = 's3Storage.custom_storages.CustomStaticStorage'


# MEDIA SETTINGS
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# MEDIA_URL = 'https://{0}/'.format(AWS_S3_CUSTOM_DOMAIN_MEDIA)
# DEFAULT_FILE_STORAGE = 's3Storage.custom_storages.CustomMediaStorage'
