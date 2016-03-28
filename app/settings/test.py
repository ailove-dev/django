# -*- coding: utf-8 -*-

from .base import *

MANAGERS = ADMINS = ()

ALLOWED_HOSTS.extend(['{{ project_name }}.test.ailove.ru'])

DATABASES['default']['HOST'] = 'db.test.ailove.ru'
