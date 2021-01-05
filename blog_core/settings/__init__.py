import os

if os.environ.get("DJANGO_SETTINGS_MODULE") == "production":
    from .production import *
else:
    from .local import *