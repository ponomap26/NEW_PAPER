"""
Django settings for New_Portal project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u^sk!^xor#4bb4gk4bxa=y@0owlc#1$7g_ut1&#8bh@&bxvh41'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news.apps.NewsConfig',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',
    # 'django_celery_beat',

]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',

]

ROOT_URLCONF = 'New_Portal.urls'

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

WSGI_APPLICATION = 'New_Portal.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "news/static"
]

LOGIN_REDIRECT_URL = "/news/"
LOGOUT_REDIRECT_URL = "/news/"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "eveonline81@yandex.ru"
EMAIL_HOST_PASSWORD = "ghwevybodrlfbfmp"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "eveonline81@yandex.ru"

SERVER_EMAIL = "eveonline81@yandex.ru"
MANAGERS = (
    ('Ivan', 'ponomap26@yandex.ru'),
    # ('Petr', 'petr@yandex.ru'),
)

ADMINS = (
    ('anton', 'ponomap26@yandex.ru'),
)

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

SITE_URL = 'http:/127.0.0.1:8000'

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Samara'

CACHES = {
    'default': {
        'TIMEOUT': 30,

        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files')
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'formatters': {                 #FORMATTERS
        'debug-format': {
            'format': '{asctime} {levelname} {message}',
            'style': '{',
        },
        'info-format': {
            'format': '{asctime} {levelname} {module} {message}',
            'style': '{',
        },
        'warning_format': {
            'format': '{asctime} {levelname} {pathname} {message} {exc_info}',
            'style': '{',
        },
        'error-format': {
            'format': '{asctime} {levelname} {pathname} {message} {exc_info}',
            'style': '{',
        },
    },
    'loggers': {                    # LOGGERS
        'django': {
            'handlers': [
                'debug_console',
                'warning_console',
                'error_console',
                'file_info',
            ],
            'propagate': True,
        },
        'django.request': {
            'level': 'ERROR',
            'handlers': [
                'file_error',
                'mail_admins'
            ],
        },
        'django.server': {
            'level': 'ERROR',
            'handlers': [
                'file_error',
                'mail_admins'
            ],
        },
        'django.template': {
            'level': 'ERROR',
            'handlers': ['file_error'],
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['file_error'],
        },
        'django.security': {
            'level': 'DEBUG',
            'handlers': ['file_security'],
        },
    },
    'handlers': {                       # HENDLER
        'debug_console': {
            'filters': ['debug_true'],
            'formatter': 'debug-format',
            'class': 'logging.StreamHandler',
        },
        'warning_console': {
            'level': 'WARNING',
            'filters': ['debug_true'],
            'formatter': 'warning_format',
            'class': 'logging.StreamHandler',
        },
        'error_console': {
            'level': 'ERROR',
            'filters': ['debug_true'],
            'formatter': 'error-format',
            'class': 'logging.StreamHandler',
        },
        'file_info': {
            'level': 'INFO',
            'filters': ['debug_false'],
            'formatter': 'info-format',
            'class': 'logging.FileHandler',
            'filename': 'general.log',
        },
        'file_error': {
            'level': 'ERROR',
            'formatter': 'error-format',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
        },
        'file_security': {
            'level': 'INFO',
            'formatter': 'info-format',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['debug_false'],
            'formatter': 'warning_format',
            'class': 'django.utils.log.AdminEmailHandler'
        },

    },
    'filters': {            # FILTERS
        'debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },

    },
}
