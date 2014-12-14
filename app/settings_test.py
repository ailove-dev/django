# -*- coding: utf-8 -*-

from settings import *

MANAGERS = ADMINS = ()

ALLOWED_HOSTS.extend(['projectname.test.ailove.ru'])

DATABASES['default']['HOST'] = 'db.test.ailove.ru'
