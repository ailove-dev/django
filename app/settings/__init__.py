CONFIG = __import__("app.config").config

if CONFIG.SETTINGS["ENV"] == "dev":
    from .development import *  # noqa
elif CONFIG.SETTINGS["ENV"] == "local":
    try:
        from .local import *  # noqa
    except ImportError:
        from .development import *  # noqa
else:
    from .production import *  # noqa
