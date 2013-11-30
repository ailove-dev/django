configs = ('database', 'memcache', 'social', 'revision')
local_ips = ('192.168.', '127.0.0.1')

import re
import socket
from os import path
from cStringIO import StringIO
from ConfigParser import SafeConfigParser


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

for config in configs:
    filepath = path.join(PATHS['CONFIG_DIR'], config)

    if path.exists(filepath):
        parser.readfp(StringIO('[config]\n' + open(filepath, 'r').read()))

        for item in parser.items('config'):
            SETTINGS[item[0].upper()] = item[1]

if any(ip in socket.gethostbyname(socket.gethostname()) for ip in local_ips):
    SETTINGS['ENV'] = 'local'
elif path.exists(PATHS['CONFIG_DIR'] + 'production'):
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
