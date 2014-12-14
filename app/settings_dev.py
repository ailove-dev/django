# -*- coding: utf-8 -*-

from settings import *

DEBUG = True

MIDDLEWARE_CLASSES += ('app.middleware.XhrSharingMiddleware',)
