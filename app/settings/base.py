CONFIG = __import__("app.config").config

SECRET_KEY = CONFIG.env("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = ["*"]

SITE_ID = 1
SITE_URL = "https://business-class.pro"

#########################
# Application definition
#########################

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.admin",
    "bc.users",
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

WSGI_APPLICATION = "app.wsgi.application"

#########################
# Database
#########################

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": CONFIG.env("DB_NAME"),
        "USER": CONFIG.env("DB_USER"),
        "PASSWORD": CONFIG.env("DB_PASSWORD"),
        "HOST": CONFIG.env("DB_HOST"),
        "PORT": CONFIG.env("DB_PORT", str, ""),
    }
}


#########################
# Language
#########################

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = True

USE_TZ = True

#########################
# Static files
#########################


STATIC_ROOT = CONFIG.PATHS["STATIC_DIR"]

STATIC_URL = "/static/"

MEDIA_ROOT = CONFIG.PATHS["DATA_DIR"]

MEDIA_URL = "/data/"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

FILE_UPLOAD_TEMP_DIR = CONFIG.PATHS["TMP_DIR"]

SESSION_FILE_PATH = CONFIG.PATHS["TMP_DIR"]

ADMIN_URL = "admin/"

#########################
# Email settings
#########################

DEFAULT_FROM_EMAIL = ""

SERVER_EMAIL = "Google BC 2.0 <error@ailove.ru>"

MANAGERS = ADMINS = (("error", "error@ailove.ru"),)

EMAIL_SUBJECT_PREFIX = ""

#########################
# Other settings (Templates, Locale, Context)
#########################

LOCALE_PATHS = (str(CONFIG.APP_DIR.path("app", "locale")),)

AUTH_PASSWORD_VALIDATORS = ()

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(CONFIG.APP_DIR.path("app", "templates"))],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.csrf",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "debug": False,
        },
    }
]
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "stat_time": {"format": "[%(asctime)s] %(message)s"},
        "verbose": {"format": "{levelname} {asctime} {message}", "style": "{"},
    },
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {"class": "logging.StreamHandler", "formatter": "verbose"},
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        }
    },
}


AUTH_USER_MODEL = "users.User"

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "bc.views.exception_handler",
    "DATE_INPUT_FORMATS": ("%d.%m.%Y", "iso-8601"),
}

AUTHENTICATION_BACKENDS = (
    "bc.auth.backends.BusinessClassBackend",
    "django.contrib.auth.backends.ModelBackend",
)
