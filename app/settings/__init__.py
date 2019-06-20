CONFIG = __import__("app.config").config

if CONFIG.env("ENV") == "dev":
    from .development import *  # noqa
elif CONFIG.env("ENV") == "local":
    try:
        from .local import *  # noqa
    except ImportError:
        from .development import *  # noqa
else:
    from .production import *  # noqa
