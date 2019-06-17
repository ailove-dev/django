import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), "../")))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")


application = get_wsgi_application()
