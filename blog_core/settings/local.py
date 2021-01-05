from .base import *

import os
from pathlib import Path

DEBUG = True

ALLOWED_HOSTS = ['ilovedj.herokuapp.com','www.ilovedjango3000.com','ilovedjango3000.com','127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


#static
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static_dir')
]
STATIC_ROOT =os.path.join(BASE_DIR,'static_root')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media_root')

#Ckeditor configuration
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'extraPlugins': ','.join(
            [
                'codesnippet',
                'youtube',
            ]),
    },
}
CKEDITOR_UPLOAD_PATH = "uploads/"