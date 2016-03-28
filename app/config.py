# -*- coding: utf-8 -*-

import sys
import re
import socket
import dj_database_url
from os import path, environ

try:
    from io import StringIO
    from configparser import SafeConfigParser
except ImportError:
    from cStringIO import StringIO
    from ConfigParser import SafeConfigParser

ENV_APP_MODE = 'APP_MODE'
ENV_REDIS_URL = 'REDIS_URL'
ENV_ELASTIC_URL = 'ELASTIC_URL'

CONFIG_NAMES = ('database',)
LOCAL_IPS = ('192.168.', '127.0.0.1')
PATHS = SETTINGS = {}

parser = SafeConfigParser()


PATHS['APP_DIR'] = path.realpath(path.join(path.dirname(__file__), '../')) + '/'
PATHS['DATA_DIR'] = path.realpath(path.join(PATHS['APP_DIR'], '../../data')) + '/'
PATHS['CONFIG_DIR'] = path.realpath(path.join(PATHS['APP_DIR'], '../../conf')) + '/'
PATHS['TMP_DIR'] = path.realpath(path.join(PATHS['APP_DIR'], '../../tmp')) + '/'
PATHS['CACHE_DIR'] = path.realpath(path.join(PATHS['APP_DIR'], '../../cache')) + '/'

match = re.match(r'/srv/www/[a-zA-Z0-9_\-]+/repo/(?P<branch>[\w\-]+)/', PATHS['APP_DIR'])

if match is not None:
    SETTINGS['BRANCH'] = match.group('branch')
else:
    SETTINGS['BRANCH'] = 'dev'

PATHS['STATIC_DIR'] = path.realpath(path.join(PATHS['DATA_DIR'], 'static', SETTINGS['BRANCH'])) + '/'

for config in CONFIG_NAMES:
    filepath = path.join(PATHS['CONFIG_DIR'], config)

    if path.exists(filepath):
        parser.readfp(StringIO('[config]\n' + open(filepath, 'r').read()))

        for item in parser.items('config'):
            SETTINGS[item[0].upper()] = item[1]

    elif config == 'database' and not path.isfile(filepath):
        if environ.get(dj_database_url.DEFAULT_ENV, None) is None:
            sys.exit('Add file conf/database or set environment variable {}'.format(dj_database_url.DEFAULT_ENV))

if any(ip in socket.gethostbyname(socket.gethostname()) for ip in LOCAL_IPS):
    SETTINGS['ENV'] = 'local'
elif path.exists(PATHS['CONFIG_DIR'] + 'production') or environ.get(ENV_APP_MODE, None) == 'production':
    SETTINGS['ENV'] = 'prod'
elif '/test/' in PATHS['APP_DIR']:
    SETTINGS['ENV'] = 'test'
else:
    SETTINGS['ENV'] = 'dev'

if path.exists(path.join(PATHS['APP_DIR'], 'app', 'social')):
    try:
        if SETTINGS['ENV'] == 'local' or SETTINGS['ENV'] == 'prod':
            SOCIAL = __import__('app.social.' + SETTINGS['ENV'], fromlist=['social.' + SETTINGS['ENV']])
        else:
            SOCIAL = __import__('app.social.' + SETTINGS['BRANCH'], fromlist=['social.' + SETTINGS['BRANCH']])
    except ImportError:
        SOCIAL = __import__('app.social.dev', fromlist=['social.dev'])
