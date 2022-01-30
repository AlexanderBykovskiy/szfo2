import psycopg2
from pathlib import Path
from .db_config import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9*+%lovjiqals5n32s)b3kdoq68@3ql%2x@w(s^wunzqo6*gy7'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG') == 'True'

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(';')


# Application definition
INSTALLED_APPS = [
    'ckeditor',
    'ckeditor_uploader',
    'easy_thumbnails',
    'easy_thumbnails.optimize',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cleanup.apps.CleanupConfig',
    'static_pages.apps.StaticPagesConfig',
    'feedback.apps.FeedbackConfig',
    'news.apps.NewsConfig',
    'publications.apps.PublicationsConfig',
    'partners.apps.PartnersConfig',
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

ROOT_URLCONF = 'szfo.urls'


# Template

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR]
        ,
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

WSGI_APPLICATION = 'szfo.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = env('LANGUAGE_CODE')

TIME_ZONE = env('TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    'szfo/static/',
]


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'


# CKeditor

CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            [
                'Undo', 'Redo',
                '-', 'Maximize', 'Source',
                'Format',
                '-', 'Font', 'FontSize',
                '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock',
                '-', 'Outdent', 'Indent',
                # '-', 'Scayt',
            ],
            [
                '-', 'Bold', 'Italic', 'Underline', 'TextColor',
                '-', 'NumberedList', 'BulletedList',
                '-', 'Link', 'Unlink', 'Anchor',
                '-', 'Image', 'Table', 'HorizontalRule', 'Blockquote',
            ]
        ],
        'height': 500,
        'width': '100%',
        'toolbarCanCollapse': False,
        'forcePasteAsPlainText': True,
        'extraPlugins': ','.join([
            'uploadimage',
            'div',
            'divarea',
            'link',
            'scayt',
            'showblocks',
            'sourcedialog',
            'uploadwidget',
        ]),
        'extraAllowedContent': 'span; nav; svg; path; g; style; stop; linearGradient; circle; *[*]; *(*);',
        'disallowedContent': 'img{width,height}'
    }
}


# Easy-thumbnails
THUMBNAIL_ALIASES = {
    '': {
        'publication-xxs': {'size': (300, 225), 'crop': True},
        'publication-xs': {'size': (400, 300), 'crop': True},
        'publication-sm': {'size': (640, 425), 'crop': True},
        'publication-md': {'size': (768, 512), 'crop': True},
        'publication-lg': {'size': (1024, 680), 'crop': True},
        'publication-xl': {'size': (1280, 850), 'crop': True},

        'publication-xxs-long': {'size': (300, 150), 'crop': True},
        'publication-xs-long': {'size': (400, 200), 'crop': True},
        'publication-sm-long': {'size': (640, 320), 'crop': True},
        'publication-md-long': {'size': (768, 384), 'crop': True},
        'publication-lg-long': {'size': (1024, 512), 'crop': True},
        'publication-xl-long': {'size': (1280, 640), 'crop': True},

        'carousel-logo': {'size': (200, 200), 'crop': True},

        'og-image': {'size': (1200, 630), 'crop': True},
    },
}
