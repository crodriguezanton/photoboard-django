from common_settings import *
import raven


""" Static files and media (CSS, JavaScript, Images) """
STATICFILES_DIRS = []
ENV_PATH = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, 'static_server/media/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static_server/static/')

# This one is just useful during development, on production statics and media should be served by nginx / apache
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'photoboard',
            'USER': 'photoboard',
            'PASSWORD': 'joule2016',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

RAVEN_CONFIG = {
    'dsn': 'https://ee7d4730069e4fffba02fcaf1ead0ad9:e919136a74d3496dbfa3b195a5c81b9d@sentry.io/123742',
    # If you are using git, you can also automatically configure the
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING', # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/photoboard/debug.log',
        }
    },
    'loggers': {
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['file'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': False,
        },
    },
}