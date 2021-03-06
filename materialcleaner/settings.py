"""
Django settings for materialcleaner project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b6c)%vc*$14r!o#&_nf8b5752s_g*-o8*b5!^*l!fi8%d2as*2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# !!!
# TO HAVE PROPER PERMISSION IDs please MIGRATE DB acc. file:
# 0001_initial.py dated # Generated by Django 2.2.10 on 2020-03-12 22:01
# !!!
AUTHORISATION_RULES = 'AUTHORISATION RULES means:\n' \
                      ' - login with:\n' \
                      '     - username or email or phone\n' \
                      '     - raw password\n' \
                      ' - authorisation with:\n' \
                      '     - user identification: checking if given username or email or phone is in the DB\n' \
                      '     - checking if identified user is active acc. DB (automatic check by Django)\n' \
                      '     - checking if identified user has the same hashed password as given hashed password\n' \
                      '     - taking group of identified user (so therefore its permissions acc. ACCESS POLICIES)'

ACCESS_POLICIES = 'ACCESS POLICIES (after authentication). User groups and their permissions:' \
                  ' - superuser: has ALL permissions, so does not have to join any group,\n' \
                  ' - staff: has ALL permissions EXCEPT:\n' \
                  '     - User & UserDetail: Create/Update/Delete (Delete - only through "active" field),\n' \
                  '     - logentry: Create/Update/Delete,\n' \
                  '     - Group: Create/Update/Delete,\n' \
                  '     - Permission: Create/Update/Delete,\n' \
                  '     - contenttype: Create/Update/Delete,\n' \
                  '     - session: Create/Update/Delete,\n' \
                  ' - regular (sellers/buyers): has permissions ONLY to:\n' \
                  '     - SalePoster: all Read,\n' \
                  '     - SalePoster: own Create/Update/Delete,\n' \
                  '     - User & UserDetail: own Create/Update WITHOUT setting staff, active, etc. DB fields; NO DELETE!!!\n' \
                  'Above all users should be authenticated (inactive users can not login & authorised)\n' \
                  '\n' \
                  'Not authenticated users may only:\n' \
                  '     - SalePoster: all Read\n' \
                  '     - login'

# User groups acc. ACCESS_POLICIES:
GROUP_TYPES = ('staff',
               'regular'
               )

# Forbidden permissions for staff user's group acc. ACCESS_POLICIES:
PERMISSIONS_FORBIDDEN_FOR_STAFF = ('add_user',
                                   'change_user',
                                   'delete_user',
                                   'add_userdetail',
                                   'change_userdetail',
                                   'delete_userdetail',
                                   'add_logentry',
                                   'change_logentry',
                                   'delete_logentry',
                                   'add_group',
                                   'change_group',
                                   'delete_group',
                                   'add_permission',
                                   'change_permission',
                                   'delete_permission',
                                   'add_contenttype',
                                   'change_contenttype',
                                   'delete_contenttype',
                                   'add_session',
                                   'change_session',
                                   'delete_session',
                                   )

# Permissions for regular user's group acc. ACCESS_POLICIES:
PERMISSIONS_FOR_REGULARS = ('add_user',
                            'change_user',
                            'delete_user',
                            'view_user',
                            'add_userdetail',
                            'change_userdetail',
                            'delete_userdetail',
                            'view_userdetail',
                            'add_saleposter',
                            'change_saleposter',
                            'delete_saleposter',
                            'view_saleposter',
                            )

# Basic photo's file types
FILE_PHOTO_TYPES_BASIC = [
    ('image/jpeg'),
    ('image/bmp'),
    ('image/gif'),
    ('image/png'),
    ('image/tiff'),
    ('image/webp'),
]

# Basic's poster categories
CATEGORIES_BASIC = [
    {'en': 'brick debris', 'pl': 'gruz ceglany'},
    {'en': 'reinforced concrete debris', 'pl': 'gruz żelbetowy'},
    {'en': 'bricks', 'pl': 'cegły'},
    {'en': 'toilet seats', 'pl': 'sedesy'},
]

# Regions/Wojwództwa of Poland
REGIONS = (
    ('D', 'dolnośląskie'),
    ('C', 'kujawsko-pomorskie'),
    ('L', 'lubelskie'),
    ('F', 'lubuskie'),
    ('E', 'łódzkie'),
    ('K', 'małopolskie'),
    ('W', 'mazowieckie'),
    ('O', 'opolskie'),
    ('R', 'podkarpackie'),
    ('B', 'podlaskie'),
    ('G', 'pomorskie'),
    ('S', 'śląskie'),
    ('T', 'świętokrzyskie'),
    ('N', 'warmińsko-mazurskie'),
    ('P', 'wielkopolskie'),
    ('Z', 'zachodniopomorskie'),
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'i18n',
    'poster',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # specific for i18N
]

ROOT_URLCONF = 'materialcleaner.urls'

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

WSGI_APPLICATION = 'materialcleaner.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'HOST': '127.0.0.1',
        'NAME': 'matcln',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'postgres',
        'PASSWORD': 'coderslab',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Translation (part of Internationalization)
# Provide a lists of languages which your site supports.
# https://docs.djangoproject.com/en/dev/topics/i18n/translation/#how-django-discovers-language-preference
LANGUAGES = (
    ('en', _('English')),
    ('pl', _('polski')),
)
# Set the default language (recommended English)
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'en'
TIME_ZONE = 'CET'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# A list of directories where Django looks for translation files
# https://docs.djangoproject.com/en/3.0/ref/settings/#locale-paths
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),  # Optional, default path './locales' folder for app's translation files
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'

# Managing storage user-upload files
# (must be different from STATIC_ROOT or STATIC_URL due to security risks (if you are accepting
# uploaded content from untrusted users)
# No "/" at the begining (with "/" issue with open() built-in function)
# https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-MEDIA_ROOT
MEDIA_ROOT = 'poster/media/upload/'
MEDIA_URL = ''
