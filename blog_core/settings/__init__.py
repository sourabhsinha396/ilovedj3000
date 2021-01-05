import os

if os.environ.get("DJANGO_SETTINGS_USE") == "production":
    from .production import *
else:
    from .local import *