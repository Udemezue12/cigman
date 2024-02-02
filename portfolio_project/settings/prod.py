from .common import *
import os
import dj_database_url


SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False
ALLOWED_HOSTS = []

PORT = int(os.environ.get('PORT', 8080))

DATABASE_URL = os.getenv('DATABASE_URL')

db_from_env = dj_database_url.config(default=DATABASE_URL)

# Update the DATABASES setting
DATABASES = {
    'default': db_from_env,
    'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
}


EMAIL_HOST = os.environ.get('MAILTRAP_SMTP_SERVER')
EMAIL_PORT = os.environ.get('MAILTRAP_SMTP_PORT')
EMAIL_HOST_USER = os.environ.get('MAILTRAP_SMTP _LOGIN')
EMAIL_PASSWORD= os.environ.get('MAILTRAP_SMTP_PASSWORD')
DEFAULT_FROM_EMAIL= ['udemezue0009@gmail.com']

REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/1')

# Update CELERY_BROKER_URL if you are using Celery with Redis
CELERY_BROKER_URL = REDIS_URL

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 10 * 60,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
