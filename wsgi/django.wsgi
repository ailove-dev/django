import os
import sys

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

from django.conf import settings
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

if settings.CONFIG.SETTINGS['ENV'] == 'local':
    try:
        import uwsgi
    except ImportError:
        import app.monitor
        app.monitor.start(interval=1.0)
