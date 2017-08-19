'''
WSGI config for my project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
'''

import os

from django.core.wsgi import get_wsgi_application

from common.secret import Secret


ROOT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '../')
secret = Secret(ROOT_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my.settings.' + secret.get(Secret.ENVIRONMENT))

application = get_wsgi_application()
