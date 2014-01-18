import os
import sys

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

import django.core.handlers.wsgi
from django.conf import settings

application = django.core.handlers.wsgi.WSGIHandler()

if settings.CONFIG.SETTINGS['ENV'] == 'local':
    try:
        import uwsgi
    except ImportError:
        import app.monitor
        app.monitor.start(interval=1.0)
