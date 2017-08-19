import json

import os
from django.core.exceptions import ImproperlyConfigured


class Secret(object):
    SECRET_FILE_NAME = 'secrets.json'

    SECRET_KEY = "secret_key"
    ENVIRONMENT = "environment"

    # private member
    __secrets = None

    def __init__(self, root_dir: str):
        secret_file_path = os.path.join(root_dir, Secret.SECRET_FILE_NAME)

        try:
            with open(secret_file_path) as f:
                self.__secrets = json.loads(f.read())
        except (OSError, IOError):
            raise ImproperlyConfigured('There is no setting file - ' + secret_file_path)

    def get(self, setting):
        try:
            return self.__secrets[setting]
        except KeyError:
            error_msg = 'Set the {} environment variable!'.format(setting)
            raise ImproperlyConfigured(error_msg)
