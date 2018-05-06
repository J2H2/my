# noinspection PyUnresolvedReferences
from .base import *  # flake8: noqa: F403  # pylint:disable=wildcard-import

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ('my.jun2.org', 'www.jun2.org', 'jun2.org',)
CORS_ORIGIN_WHITELIST = ('my.jun2.org', 'www.jun2.org', 'jun2.org',)
