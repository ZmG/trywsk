import os
import sys
sys.path.append('/home/vcap')
sys.path.append('/home/vcap/app')
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.bluemix'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
