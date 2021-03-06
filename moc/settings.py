"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 1.11a1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
import sys
from libs import common


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nvc3q0w4ihq-g4p$xfc_561_mpbu@+gboy#934maxa5=b3fmda'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'moc.urls'

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

WSGI_APPLICATION = 'moc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

database = common.get_config()
DATABASES = database


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = ( os.path.join(BASE_DIR, 'static'), )

# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    # 格式器
    'formatters': {
       'standard': {  #日志格式
            'format': '%(asctime)s - %(message)s'
       },
        'errorFormatters': {
            'format': '%(levelname)s %(asctime)s %(pathname)s %(filename)s %(module)s %(funcName)s %(lineno)d: %(message)s'
        }
    },

    # 过滤器
    'filters': {
    },

    # 处理器
    'handlers': {
        'info': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/operate.log'),
            'maxBytes':1024 * 1024 * 5,
            'backupCount': 7,
            'formatter':'standard',
        },
        'file': {
                'level':'DEBUG',
                'class':'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(BASE_DIR, 'log/file.log'),
                'maxBytes':1024 * 1024 * 5,
                'backupCount': 7,
                'formatter':'standard',
         },
         'waring': {
                'level':'WARNING',
                'class':'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(BASE_DIR, 'log/error.log'),
                'maxBytes':1024 * 1024 * 5,
                'backupCount': 7,
                'formatter':'errorFormatters',
            }
    },

    # 记录器
    'loggers': {
        'info': {
            'handlers': ['info'],
            'level': 'DEBUG',
            'propagate': False
        },
        'file': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.request': {
            'handlers': ['waring'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django': {
            'handlers': ['waring'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}




















