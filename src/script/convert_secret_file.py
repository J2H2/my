import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))

from lib.secret.secret import SecretFileHandler  # flake8: noqa: E402

secret_file_handler = SecretFileHandler(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../'))
secret_file_handler.convert_to_encrypted_file()
