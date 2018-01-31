import json
import os

from lib.crypto.encrypt import CryptoHelper
from lib.singleton.singleton import Singleton

CRYPTO_KEY = '&Hg^C7^:y57ZqML!'
ENC_SECRET_FILE_NAME = 'enc_secrets.json'
SECRET_FILE_NAME = 'secrets.json'
VERSION_FILE_NAME = 'version'


class ImproperlyConfigured(Exception):
    pass


class Secret:
    # private member
    __secrets = None

    version = '-'

    def __init__(self):
        self._set_root_path()
        self.file_handler = SecretFileHandler(self.root_path)
        self._load()

    def get(self, key: str) -> str:
        try:
            return self.__secrets[key]
        except KeyError:
            raise ImproperlyConfigured('Set the {} environment variable!'.format(key))

    def _load(self) -> None:
        self.__secrets = json.loads(self.file_handler.load())
        self.version = self._load_version_file()

    def _load_version_file(self) -> str:
        file_path = '%s/%s' % (self.root_path, VERSION_FILE_NAME)

        try:
            with open(file_path) as file:
                return file.read().strip()
        except (OSError, IOError):
            return '-'

    def _set_root_path(self):
        self.root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


Secret = Singleton(Secret)


class SecretFileHandler:
    def __init__(self, root_path: str):
        self.root_path = root_path

    def load(self) -> str:
        enc_file_path = self._get_file_path(ENC_SECRET_FILE_NAME)

        try:
            with open(enc_file_path) as file:
                return CryptoHelper(CRYPTO_KEY).decrypt(file.read())
        except (OSError, IOError):
            raise ImproperlyConfigured('There is no setting file %s' % enc_file_path)

    def convert_to_encrypted_file(self) -> None:
        enc_string = self._encrypt_file()
        self._save_encrypted_file(enc_string)

    def _encrypt_file(self) -> str:
        file_path = self._get_file_path(SECRET_FILE_NAME)

        try:
            with open(file_path) as file:
                return CryptoHelper(CRYPTO_KEY).encrypt(file.read())
        except (OSError, IOError):
            raise ImproperlyConfigured('There is no setting file %s' % file_path)

    def _save_encrypted_file(self, enc_string: str) -> None:
        enc_file_path = self._get_file_path(ENC_SECRET_FILE_NAME)

        with open(enc_file_path, 'w') as file:
            file.write(enc_string)

    def _get_file_path(self, file_name: str) -> str:
        return os.path.join(self.root_path, file_name)
