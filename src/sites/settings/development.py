# noinspection PyUnresolvedReferences
from .base import *  # flake8: noqa: F403  # pylint:disable=wildcard-import

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ('dev.jun2.org', )
CORS_ORIGIN_WHITELIST = ('dev.jun2.org', )
