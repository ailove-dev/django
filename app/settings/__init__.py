# -*- coding: utf-8 -*-

CONFIG = __import__('app.config').config

if CONFIG.SETTINGS['ENV'] == 'test':
    from .test import *
elif CONFIG.SETTINGS['ENV'] == 'dev':
    from .development import *
elif CONFIG.SETTINGS['ENV'] == 'local':
    try:
        from .local import *
    except ImportError:
        from .development import *
else:
    from .production import *
