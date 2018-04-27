from config.common_settings import *

DEBUG = False

assert SECRET_KEY is not None, (
    'Please provide DJANGO_SECRET_KEY '
    'environment variable with a value')


ALLOWED_HOSTS += [
    os.getenv('DJANGO_ALLOWED_HOSTS'),
]

DATABASES['default'].update({
    'NAME': os.getenv('DJANGO_DB_NAME'),
    'USER': os.getenv('DJANGO_DB_USER'),
    'PASSWORD': os.getenv('DJANGO_DB_PASSWORD'),
    'HOST': os.getenv('DJANGO_DB_HOST'),
    'PORT': os.getenv('DJANGO_DB_PORT'),
})

LOGGING['handlers']['main'] = {
    'class': 'logging.handlers.WatchedFileHandler',
    'level': 'DEBUG',
    'filename': os.getenv('DJANGO_LOG_FILE')
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'default-locmemcache',
        'TIMEOUT': int(os.getenv('DJANGO_CACHE_TIMEOUT'), ),
    }
}

# file uploads

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY_ID')
AWS_STORAGE_BUCKET_NAME = os.getenv('DJANGO_UPLOAD_S3_BUCKET')

