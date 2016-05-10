# Django settings for trywsk project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG


import os
#import boto.s3.connection
#settings_dir = os.path.dirname(__file__)
#PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
from unipath import Path
PROJECT_ROOT = Path(__file__).ancestor(2)


ADMINS = (
    ('IBM jStart', 'jstart@us.ibm.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"

#AWS_STORAGE_BUCKET_NAME = 'www.docker.io-media'
#MEDIA_URL = 'https://s3.amazonaws.com/{}/'.format(AWS_STORAGE_BUCKET_NAME)

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    PROJECT_ROOT.child('assets'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# Make this unique, and don't share it with anybody.

# We store the secret key in our environment variables.
try:
    SECRET_KEY = os.environ['SECRET_KEY']
except KeyError as e:
    print "Secret key not found, using a default key, please set the SECRET_KEY in your environment"
    SECRET_KEY = "ABCDEFG22"
    pass


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
    "django.core.context_processors.media"
)

MIDDLEWARE_CLASSES = (
    # 'django.middleware.cache.UpdateCacheMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# Local memory caching. We only have a couple of non-dynamic pages, but they are
# being generated dynamically... So, we might as well cache the whole thing in memory.
CACHES = {
    'default': {  # for session data
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cachetable',
    },
    'database_cache': {  # for tweets
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'dbcache1',
    },
    'LocMemCache': {  # used for storing the mailchimp object
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    },
    'disk_cache': {  # former tweet cache
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': PROJECT_ROOT.child('cache'),
    },
}


# CACHE_MIDDLEWARE_ALIAS = default
# CACHE_MIDDLEWARE_SECONDS = 600 # default
# CACHE_MIDDLEWARE_KEY_PREFIX = '' # default



ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_ROOT.child('templates'),
    PROJECT_ROOT.child('_pages'),
)

PREREQ_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_extensions',
    'intercom',
    'analytical',
    'mailchimp',
    'markdown_deux',
    'south',
    'wsk_tutorial',
    'storages'
)

PROJECT_APPS = (
    'base',
)

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}



# see https://github.com/trentm/django-markdown-deux for optional markdown settings

MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": {
            "code-friendly": None,
        },
        "safe_mode": None,
    },
}




# analytics and tracking settings


# allowed hosts is set to *, because otherwise the website othwersise is killed by the cloud ckeck
# Besides, it would otherwise need to be set to .docker.io and *.amazonaws.com which would basically mean anyone
# can set up a copy of this site anyways without making any changes.
# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['.mybluemix.net']  # need to set to real prod value.

try:
    MAILCHIMP_API_KEY = os.environ['MAILCHIMP_API_KEY']
except KeyError:
    # Mailchimp will output a warning that it is not set.
    print "warning: MAILCHIMP API KEY NOT SET IN ENVIRONMENT"
    MAILCHIMP_API_KEY = "dummy_api_key"


# For storing files in S3
#AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
#AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#AWS_S3_CALLING_FORMAT = boto.s3.connection.OrdinaryCallingFormat()

