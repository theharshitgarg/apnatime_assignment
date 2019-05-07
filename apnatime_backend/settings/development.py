from apnatime_backend.settings.common import *

DEBUG = True

# Last entry for teting purpose
# TODO : REMOVE BEFORE PRODUCTION
ALLOWED_HOSTS = ['common-workspace-harshitgarg.c9users.io', 'localhost', 'demo-apnatime.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER_NAME'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
    }
}
