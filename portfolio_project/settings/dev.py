from .common import *
from decouple import config


SECRET_KEY = config('SECRET_KEY')


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'HOST': config('DB_HOST'),
        'PASSWORD': config('DB_PASSWORD'),
        'USER': config('DB_USER'),
        # 'OPTIONS': {
        #     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        # },
    }
}
