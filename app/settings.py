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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': CONFIG.SETTINGS['DB_NAME'],                 # Or path to database file if using sqlite3.
        'USER': CONFIG.SETTINGS['DB_USER'],                 # Not used with sqlite3.
        'PASSWORD': CONFIG.SETTINGS['DB_PASSWORD'],         # Not used with sqlite3.
        'HOST': CONFIG.SETTINGS['DB_HOST'],                 # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                                         # Set to empty string for default. Not used with sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# The directory where uploaded files larger than FILE_UPLOAD_MAX_MEMORY_SIZE will be stored
FILE_UPLOAD_TEMP_DIR = CONFIG.PATHS['TMP_DIR']

# Set this to control where Django stores session files in case if file-based session storage is used
SESSION_FILE_PATH = CONFIG.PATHS['TMP_DIR']

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = CONFIG.PATHS['DATA_DIR']

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/data/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = CONFIG.PATHS['STATIC_DIR']

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    CONFIG.PATHS['APP_DIR'] + 'app/static/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# A tuple of directories where Django looks for translation files
LOCALE_PATHS = (
    CONFIG.PATHS['APP_DIR'] + 'app/locale/',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'put_your_key_here'

# CKEditor directory for uploaded files
CKEDITOR_UPLOAD_PATH = MEDIA_ROOT + 'ckeditor/admin'

# CKEditor main config
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar':
        [
            { 'name': 'document',    'items' : [ 'Source' ] },
            { 'name': 'clipboard',   'items' : [ 'Cut','Copy','Paste','PasteText','PasteFromWord','-','Undo','Redo' ] },
            { 'name': 'editing',     'items' : [ 'Find','Replace','-','SelectAll','-','SpellChecker', 'Scayt' ] },
            { 'name': 'basicstyles', 'items' : [ 'Bold','Italic','Underline','Strike','Subscript','Superscript','-','RemoveFormat' ] },
            '/',
            { 'name': 'paragraph',   'items' : [ 'NumberedList','BulletedList','-','Outdent','Indent','-','Blockquote','CreateDiv','-','JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock','-','BidiLtr','BidiRtl' ] },
            { 'name': 'links',       'items' : [ 'Link','Unlink','Anchor' ] },
            { 'name': 'insert',      'items' : [ 'Image','Flash','Table','HorizontalRule','Smiley','SpecialChar' ] },
            '/',
            { 'name': 'styles',      'items' : [ 'Styles','Format','Font','FontSize' ] },
            { 'name': 'colors',      'items' : [ 'TextColor','BGColor' ] },
            { 'name': 'tools',       'items' : [ 'Maximize', 'ShowBlocks' ] }
        ],
        'filebrowserImageBrowseUrl': '/admin/filebrowser/browse?pop=3',
        'removeDialogTabs': 'link:upload;image:Upload;flash:Upload',
        'height': 300,
        'width': 755,
    },
}

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

# Template context processors
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

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'app.wsgi.application'

TEMPLATE_DIRS = (
    CONFIG.PATHS['APP_DIR'] + 'app/templates/',
)

INSTALLED_APPS = (
    'ckeditor',
    'south',
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

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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

if CONFIG.SETTINGS['ENV'] == 'test':
    from settings_test import *
if CONFIG.SETTINGS['ENV'] == 'dev' or CONFIG.SETTINGS['ENV'] == 'local':
    from settings_dev import *
