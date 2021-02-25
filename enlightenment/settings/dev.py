from .base import *  # noqa

# Development Database Config

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa
    }
}

DEBUG = True

ALLOWED_HOSTS = []

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # noqa

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"  # noqa
