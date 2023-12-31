"""
Django settings for ISEF01_Quizsystem project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import pymysql
from pathlib import Path

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# TODO: DEBUG auf false setzen

ALLOWED_HOSTS = [".isef01quiz.pro", "localhost"]
# TODO: localhost in ALLOWED_HOST rausnehmen
CSRF_TRUSTED_ORIGINS = ['https://isef01quiz.pro', 'https://www.isef01quiz.pro']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Core',
    'Login',
    'Logout',
    'FrageErstellen',
    'MeineInhalte',
    'FrageAnzeigen',
    'FrageBearbeiten',
    'AntwortErstellen',
    'AntwortBearbeiten',
    'Startseite',
    'Quiz',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ISEF01_Quizsystem.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'ISEF01_Quizsystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django_psdb_engine',
    'NAME': os.environ.get('DB_NAME'),
    'HOST': os.environ.get('DB_HOST'),
    'PORT': os.environ.get('DB_PORT'),
    'USER': os.environ.get('DB_USER'),
    'PASSWORD': os.environ.get('DB_PASSWORD'),
    # Zum lokalen Testen bzgl. SSL:  {'disabled': True}
    # Korrekt: SSL: {'ca': os.environ.get('MYSQL_ATTR_SSL_CA')
    'OPTIONS': {'ssl': {'ca': os.environ.get('MYSQL_ATTR_SSL_CA')},
                'charset': 'utf8mb4'}
  }
}


# User validation
AUTH_USER_MODEL = 'Core.Benutzer'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.' +
        'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' +
        'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' +
        'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' +
        'NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'de-DE'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_TZ = True

SESSION_COOKIE_AGE = 14400  # 4-Stunden-Session (Sekunden)

SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Session nach schließen nicht löschen

# Static files (CSS, JavaScript, Images)

# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Für statische Dateien
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static'),
)
#STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
STATIC_ROOT = '/var/www/isef01quiz.pro/static'
