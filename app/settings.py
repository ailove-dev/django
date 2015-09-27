# -*- coding: utf-8 -*-

CONFIG = __import__('app.config').config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

SECRET_KEY = '{{ secret_key }}'

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    # main
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third-party
    'filebrowser',
    'grappelli.dashboard',
    'common',
    'love_utils',
    'ckeditor',
    # project
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': CONFIG.SETTINGS['DB_NAME'],
        'USER': CONFIG.SETTINGS['DB_USER'],
        'PASSWORD': CONFIG.SETTINGS['DB_PASSWORD'],
        'HOST': CONFIG.SETTINGS['DB_HOST'],
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_DIRS = (
    CONFIG.PATHS['APP_DIR'] + 'app/static/',
)

STATIC_ROOT = CONFIG.PATHS['STATIC_DIR']

STATIC_URL = '/static/'

MEDIA_ROOT = CONFIG.PATHS['DATA_DIR']

MEDIA_URL = '/data/'

FILE_UPLOAD_TEMP_DIR = CONFIG.PATHS['TMP_DIR']


# Email settings

DEFAULT_FROM_EMAIL = 'info@{{ project_name }}.ru'

SERVER_EMAIL = '{{ project_name }}.ru <error@ailove.ru>'

MANAGERS = ADMINS = (('error', 'error@ailove.ru'),)

EMAIL_SUBJECT_PREFIX = ''


# Other settings (Templates, Locale, Context)

LOCALE_PATHS = (
    CONFIG.PATHS['APP_DIR'] + 'app/locale/',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            CONFIG.PATHS['APP_DIR'] + 'app/templates/',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.csrf',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Testing and logging

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        'py.warnings': {
            'handlers': ['console'],
        },
    }
}

# Third-party Application

# CKEditor

CKEDITOR_UPLOAD_PATH = MEDIA_ROOT + 'ckeditor/admin'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar':
        [
            {'name': 'document', 'items': ['Source']},
            {'name': 'clipboard', 'items': [
                'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-',
                'Undo', 'Redo'
            ]},
            {'name': 'editing', 'items': [
                'Find', 'Replace', '-', 'SelectAll', '-',
                'SpellChecker', 'Scayt'
            ]},
            {'name': 'basicstyles', 'items': [
                'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-',
                'RemoveFormat'
            ]},
            '/',
            {'name': 'paragraph', 'items': [
                'NumberedList', 'BulletedList', '-',
                'Outdent', 'Indent', '-',
                'Blockquote', 'CreateDiv', '-',
                'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-',
                'BidiLtr', 'BidiRtl'
            ]},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert', 'items': [
                'Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar'
            ]},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']}
        ],
        'filebrowserImageBrowseUrl': '/admin/filebrowser/browse?pop=3',
        'removeDialogTabs': 'link:upload;image:Upload;flash:Upload',
        'height': 300,
        'width': 755,
    },
}

# Grappelli

GRAPPELLI_ADMIN_TITLE = '{{ project_name }}'
GRAPPELLI_INDEX_DASHBOARD = 'app.dashboard.CustomIndexDashboard'

# Filebrowser

FILEBROWSER_DIRECTORY = ''
FILEBROWSER_ADMIN_THUMBNAIL = 'medium'


if CONFIG.SETTINGS['ENV'] == 'test':
    from settings_test import *
if CONFIG.SETTINGS['ENV'] == 'dev' or CONFIG.SETTINGS['ENV'] == 'local':
    from settings_dev import *

try:
    from settings_local import *
except ImportError:
    pass
