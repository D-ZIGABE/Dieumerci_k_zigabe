#import dj_database_url
from dieumerci_k_zigabe.settings import *


DEBUG = True
TEMPLATE_DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']
#INSTALLED_APPS +=['storages',] #appli de stock
#for heroku
#DATABASES['default'] = dj_database_url.config()
#for RDS AWS
#db_from_env = dj_database_url.config(conn_max_age=600)
#DATABASES['default'].update(db_from_env)



MIDDLEWARE +=['whitenoise.middleware.WhiteNoiseMiddleware',]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' 
ALLOWED_HOSTS = ['web-production-89dd.up.railway.app',]
CSRF_TRUSTED_ORIGINS = ['https://web-production-89dd.up.railway.app/',]

"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
#EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
#EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
"""
#IAM INDOEMATION
#AWS_ACCESS_KEY_ID =os.environ['AWS_ACCESS_KEY_ID']
#AWS_SECRET_ACCESS_KEY =os.environ['AWS_SECRET_ACCESS_KEY']
#S3 name
#AWS_STORAGE_BUCKET_NAME =os.environ['AWS_STORAGE_BUCKET_NAME']

#AWS_S3_FILE_OVERWRITE = False
#AWS_DEFAULT_ACL = None
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
