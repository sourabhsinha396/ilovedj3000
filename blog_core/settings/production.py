from .base import *

import os
from pathlib import Path

DEBUG = False

ALLOWED_HOSTS = ['ilovedj.herokuapp.com','www.ilovedjango3000.com','ilovedjango3000.com']


AWS_ACCESS_KEY_ID = os.environ.get("AwsDjKey")
AWS_SECRET_ACCESS_KEY = os.environ.get("AwsDjSecret")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AwsDjBucket")
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_DEFAULT_ACL = 'public-read'

AWS_LOCATION = 'static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_dir'),
]

STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'blog_core.storages.MediaStore'

 #Postges
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

DBBACKUP_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DBBACKUP_STORAGE_OPTIONS = {
    'access_key': os.environ.get("AwsDjKey"),
    'secret_key': os.environ.get("AwsDjSecret"),
    'bucket_name': os.environ.get("AwsDjBucket"),
    'default_acl': 'private',
    'location': "backups/"
}

#cron-job
CRON_CLASSES = [
    "apps.blogs.cron.DbBackup",
]