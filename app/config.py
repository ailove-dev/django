configs = ['database', 'memcache', 'social', 'revision']

from os import path
from cStringIO import StringIO
from ConfigParser import SafeConfigParser

PATHS = SETTINGS = {}
parser = SafeConfigParser()

PATHS['APP_DIR'] = path.realpath(path.join(path.dirname(__file__), '../')) + '/'
PATHS['DATA_DIR'] = path.realpath(path.join(PATHS['APP_DIR'], '../../data')) + '/'
PATHS['STATIC_DIR'] = path.realpath(path.join(PATHS['APP_DIR'], 'htdocs')) + '/'
PATHS['CONFIG_DIR'] = path.realpath(path.join(PATHS['APP_DIR'], '../../conf')) + '/'
PATHS['TMP_DIR'] = path.realpath(path.join(PATHS['APP_DIR'], '../../tmp')) + '/'
PATHS['CACHE_DIR'] = path.realpath(path.join(PATHS['APP_DIR'], '../../cache')) + '/'

for config in configs:
    file = path.join(PATHS['CONFIG_DIR'], config)

    if path.exists(file):
        parser.readfp(StringIO('[config]\n' + open(file, 'r').read()))

        for item in parser.items('config'):
            SETTINGS[item[0].upper()] = item[1]

if path.exists(PATHS['CONFIG_DIR'] + 'production'):
    SETTINGS['ENV'] = 'prod'
elif '/test/' in PATHS['APP_DIR']:
    SETTINGS['ENV'] = 'test'
else:
    SETTINGS['ENV'] = 'dev'
