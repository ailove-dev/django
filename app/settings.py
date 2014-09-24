# -*- coding: utf-8 -*-

CONFIG = __import__('app.config').config

# Debug settings
TEMPLATE_DEBUG = DEBUG = False

# Project's title which will be shown in admin interface
GRAPPELLI_ADMIN_TITLE = 'Project Name'

# Default project dashboard, you probably won't need to change it
GRAPPELLI_INDEX_DASHBOARD = 'app.dashboard.CustomIndexDashboard'

# Don't change this for filebrowser to work properly
FILEBROWSER_DIRECTORY = ''

# Default filebrowser admin thumbnail size
FILEBROWSER_ADMIN_THUMBNAIL = 'medium'

# Default email address to use for various automated correspondence from the site manager(s).
DEFAULT_FROM_EMAIL = 'info@projectname.ru'

# The email address that error messages come from, such as those sent to ADMINS and MANAGERS.
SERVER_EMAIL = 'projectname.ru <error@ailove.ru>'

# A tuple that lists people who get code error notifications. When DEBUG=False and a view raises
# an exception, Django will email these people with the full exception information. Each member
# of the tuple should be a tuple of (Full name, email address).
MANAGERS = ADMINS = (('error', 'error@ailove.ru'),)

# Subject-line prefix for email messages
EMAIL_SUBJECT_PREFIX = ''

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
    'django.contrib.admin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
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

ALLOWED_HOSTS = ['*']

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'put_your_key_here'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

# The directory where uploaded files larger than FILE_UPLOAD_MAX_MEMORY_SIZE will be stored
FILE_UPLOAD_TEMP_DIR = CONFIG.PATHS['TMP_DIR']

# Set this to control where Django stores session files in case if file-based session storage is used
SESSION_FILE_PATH = CONFIG.PATHS['TMP_DIR']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

MEDIA_ROOT = CONFIG.PATHS['DATA_DIR']

MEDIA_URL = '/data/'

STATIC_ROOT = CONFIG.PATHS['STATIC_DIR']

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    CONFIG.PATHS['APP_DIR'] + 'app/static/',
)

LOCALE_PATHS = (
    CONFIG.PATHS['APP_DIR'] + 'app/locale/',
)

# CKEditor directory for uploaded files
CKEDITOR_UPLOAD_PATH = MEDIA_ROOT + 'ckeditor/admin'

# CKEditor main config
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

ROOT_URLCONF = 'app.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'app.wsgi.application'

TEMPLATE_DIRS = (
    CONFIG.PATHS['APP_DIR'] + 'app/templates/',
)

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

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

if CONFIG.SETTINGS['ENV'] == 'test':
    from settings_test import *
if CONFIG.SETTINGS['ENV'] == 'dev' or CONFIG.SETTINGS['ENV'] == 'local':
    from settings_dev import *
