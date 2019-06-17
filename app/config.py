import re
import typing
from configparser import ConfigParser
from os import path

import environ

ENV_APP_MODE = "APP_MODE"

CONFIG_NAMES = ("database", "secrets")
LOCAL_IPS = ("192.168.", "127.0.0.1")
PATHS = {}
SETTINGS: typing.Dict[str, typing.Any] = {}


class EnvWithParser(environ.Env):
    def __call__(self, var, cast=None, default=environ.Env.NOTSET, parse_default=False):
        return super().__call__(var, cast, SETTINGS.get(var, default), parse_default)


env = EnvWithParser()

APP_DIR = environ.Path(__file__) - 2
DATA_DIR = APP_DIR.path("..", "..", "data")
CONFIG_DIR = APP_DIR.path("..", "..", "conf")
env.read_env(str(APP_DIR.path(".env")))

parser = ConfigParser()


PATHS["APP_DIR"] = str(APP_DIR)
PATHS["DATA_DIR"] = str(DATA_DIR)
PATHS["LOG_DIR"] = str(APP_DIR.path("..", "..", "logs"))
PATHS["CONFIG_DIR"] = str(CONFIG_DIR)
PATHS["TMP_DIR"] = str(APP_DIR.path("..", "..", "tmp"))
PATHS["CACHE_DIR"] = str(APP_DIR.path("..", "..", "cache"))
match = re.match(
    r"/srv/www/[a-zA-Z0-9_\-]+/repo/(?P<branch>[\w\-]+)/", PATHS["APP_DIR"]
)

if match is not None:
    SETTINGS["BRANCH"] = match.group("branch")
else:
    SETTINGS["BRANCH"] = "dev"

PATHS["STATIC_DIR"] = str(DATA_DIR.path("static", SETTINGS["BRANCH"]))

for config in CONFIG_NAMES:
    filepath = CONFIG_DIR.path(config)

    if not path.exists(str(filepath)):
        continue

    with filepath.open("r") as file:
        parser.read_string(f"[config]\n{file.read()}")

        for key, value in parser.items("config"):
            SETTINGS[key.upper()] = value

if path.exists(str(CONFIG_DIR.path("production"))):
    SETTINGS["ENV"] = "prod"
else:
    env_app_mode = env(ENV_APP_MODE, str, default="dev")
    if env_app_mode == "production":
        SETTINGS["ENV"] = "prod"
    else:
        SETTINGS["ENV"] = env_app_mode or "dev"
