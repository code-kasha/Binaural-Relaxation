from .base import *  # noqa

with open(SECRETS_DIR / ".db_user") as f:  # noqa
    DB_USER = f.read().strip()

with open(SECRETS_DIR / ".db_pass") as f:  # noqa
    DB_PASS = f.read().strip()


# Staging Database Config

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "nlight",
        "USER": DB_USER,
        "PASSWORD": DB_PASS,
        "HOST": "localhost",
        "PORT": 5432,
    }
}

DEBUG = True

ALLOWED_HOSTS = ["*"]

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # noqa

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"  # noqa
