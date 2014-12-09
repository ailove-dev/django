# -*- coding: utf-8 -*-

CONFIG = __import__('app.config').config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

SECRET_KEY = r'put_your_key_here'

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'ckeditor',
    'utilities.capable',
    'utilities.templatetags.common',
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin'
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
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'
        'NAME': CONFIG.SETTINGS['DB_NAME'],                  # Or path to database file if using sqlite3
        'USER': CONFIG.SETTINGS['DB_USER'],                  # Not used with sqlite3
        'PASSWORD': CONFIG.SETTINGS['DB_PASSWORD'],          # Not used with sqlite3
        'HOST': CONFIG.SETTINGS['DB_HOST'],                  # Set to empty string for localhost. Not used with sqlite3
        'PORT': '',                                          # Set to empty string for default. Not used with sqlite3
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATICFILES_DIRS = (
    CONFIG.PATHS['APP_DIR'] + 'app/static/',
)

STATIC_ROOT = CONFIG.PATHS['STATIC_DIR']

STATIC_URL = '/static/'

MEDIA_ROOT = CONFIG.PATHS['DATA_DIR']

MEDIA_URL = '/data/'

FILE_UPLOAD_TEMP_DIR = CONFIG.PATHS['TMP_DIR']

SESSION_FILE_PATH = CONFIG.PATHS['TMP_DIR']


# Email settings

DEFAULT_FROM_EMAIL = 'info@projectname.ru'

SERVER_EMAIL = 'projectname.ru <error@ailove.ru>'

MANAGERS = ADMINS = (('error', 'error@ailove.ru'),)

EMAIL_SUBJECT_PREFIX = ''


# Other settings (Templates, Locale, Context)

LOCALE_PATHS = (
    CONFIG.PATHS['APP_DIR'] + 'app/locale/',
)

TEMPLATE_DIRS = (
    CONFIG.PATHS['APP_DIR'] + 'app/templates/',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages'
)


# Testing and logging

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
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
            {'name': 'document',    'items': ['Source']},
            {'name': 'clipboard',   'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing',     'items': ['Find', 'Replace', '-', 'SelectAll', '-', 'SpellChecker', 'Scayt']},
            {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            '/',
            {'name': 'paragraph',   'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl']},
            {'name': 'links',       'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',      'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar']},
            '/',
            {'name': 'styles',      'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors',      'items': ['TextColor', 'BGColor']},
            {'name': 'tools',       'items': ['Maximize', 'ShowBlocks']}
        ],
        'filebrowserImageBrowseUrl': '/admin/filebrowser/browse?pop=3',
        'removeDialogTabs': 'link:upload;image:Upload;flash:Upload',
        'height': 300,
        'width': 755,
    },
}

# Grappelli

GRAPPELLI_ADMIN_TITLE = 'Project Name'
GRAPPELLI_INDEX_DASHBOARD = 'app.dashboard.CustomIndexDashboard'

# Filebrowser

FILEBROWSER_DIRECTORY = ''
FILEBROWSER_ADMIN_THUMBNAIL = 'medium'


if CONFIG.SETTINGS['ENV'] == 'test':
    from settings_test import *
if CONFIG.SETTINGS['ENV'] == 'dev' or CONFIG.SETTINGS['ENV'] == 'local':
    from settings_dev import *
