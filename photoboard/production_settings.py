from common_settings import *


""" Static files and media (CSS, JavaScript, Images) """
STATICFILES_DIRS = []
ENV_PATH = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, 'static_server/media/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static_server/static/')

# This one is just useful during development, on production statics and media should be served by nginx / apache
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

DEBUG = False
ALLOWED_HOSTS = ['.photoboard.tech', '.azure.com']

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