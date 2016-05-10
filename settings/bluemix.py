# settings/bluemix.py
from settings.base import *
import os.path, os, json, urlparse

print "using bluemix settings"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/vcap/bluemix/data/media/'
STATIC_ROOT = '/home/vcap/bluemix/volatile/static/'
STATIC_URL = '/static/'

#Bluemix Service Connection Info
# MySQL configs from BlueMix
vcap_host = os.environ.get('VCAP_APP_HOST')
vcap_port = os.environ.get('VCAP_APP_PORT')
vcap_config = os.environ.get('VCAP_SERVICES')
decoded_config = json.loads(vcap_config)

for key, value in decoded_config.iteritems():
    if key.startswith('mysql'):
        db_creds = decoded_config[key][0]['credentials']
        engine = 'django.db.backends.mysql' 
    elif key.startswith('cleardb'):
        db_creds = decoded_config[key][0]['credentials']
        engine = 'django.db.backends.mysql'
    elif key.startswith('elephantsql'):
        db_creds = decoded_config[key][0]['credentials']
        pgurl = urlparse.urlparse(str(db_creds['uri']))
        db_creds['hostname']=pgurl.hostname
        if pgurl.port:
            db_creds['port']=pgurl.port
        else:
            db_creds['port']=5432
        db_creds['username']=pgurl.username
        db_creds['password']=pgurl.password
        db_creds['name']=pgurl.path[1:]
        engine = 'django.db.backends.postgresql_psycopg2'

if db_creds:
    db_host = db_creds['hostname']
    db_port = db_creds['port']  
    db_username = db_creds['username']
    db_password = db_creds['password']
    db_db = db_creds['name']
    db_url = str(db_creds['uri'])
    db_name = db_creds['name']


DATABASES = {
    'default': {
        'ENGINE': engine, #
        'NAME': db_name,
        'USER': db_username,
        'PASSWORD': db_password,
        'HOST': db_host,
        'PORT': db_port,
    }
}


log_file_dir = PROJECT_ROOT.child('docker_index.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
     'require_debug_false': {
         '()': 'django.utils.log.RequireDebugFalse'
     }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': log_file_dir,
            'maxBytes': 1024*1024*25, # 25 MB
            'backupCount': 5,
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'log_file', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console', 'log_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console', 'log_file', 'mail_admins'],
            'level': 'INFO',
            'propagate': False,
        },
        # Catch All Logger -- Captures any other logging
        '': {
            'handlers': ['console', 'log_file', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}
