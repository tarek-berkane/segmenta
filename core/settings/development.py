from core.settings.base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-wy$o%&rzx1ukorcq)cj%o2y*46*-i7+yv0vu7ct)hvkd23oc*#"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS += [
    "debug_toolbar",
    "django_browser_reload",
]


MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

INTERNAL_IPS = [
    "127.0.0.1",
]
# =======================
# LOGGING
# =======================
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}
# =======================
# EMAIL
# =======================
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# =======================
# MEDIA
# =======================
MEDIA_ROOT = BASE_DIR / "media/"
MEDIA_URL = "/media/"
STATIC_URL = "static/"
