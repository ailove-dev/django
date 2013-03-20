import os, sys, socket

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

if '192.168.' in socket.gethostbyname(socket.gethostname()):
    import app.monitor
    app.monitor.start(interval=1.0)
