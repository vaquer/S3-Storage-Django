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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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
        'NAME': 'djangos3',
        'USER': 'djangos3',
        'PASSWORD': 'django.2015.meetup',
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


#AWS CONFIGURATIONS
AWS_STORAGE_BUCKET_NAME = 'static-django-meet'
AWS_ACCESS_KEY_ID = 'AKIAJBUJY7W4K5MP6AJQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_S3_CUSTOM_DOMAIN = '{0}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# STATIC_URL = '/static/'
STATIC_AWS_STORAGE_BUCKET_NAME = 'static-django-meet'
STATIC_URL = 'https://{0}/static/'.format(AWS_S3_CUSTOM_DOMAIN)
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
# SET THIS FEATURES ONLY WITH DJANGO COMPRESSOR
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder', 
    'compressor.finders.CompressorFinder',)
STATICFILES_STORAGE = 's3Storage.custom_storages.CustomStaticStorage'


#COMPRESSOR SETTINGS
COMPRESS_ENABLED = True
COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = os.path.join(BASE_DIR, 'static')
COMPRESS_STORAGE = 's3Storage.custom_storages.CustomStaticStorage'


#MEDIA SETTINGS
MEDIA_AWS_STORAGE_BUCKET_NAME = 'media-django-meet'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'https://{0}/media/'.format(AWS_S3_CUSTOM_DOMAIN)
# DEFAULT_FILE_STORAGE = 's3Storage.custom_storages.CustomMediaStorage'