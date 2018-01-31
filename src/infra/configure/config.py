from django.conf import settings


class GeneralConfig:
    @staticmethod
    def is_dev() -> bool:
        return settings.DEBUG

    @staticmethod
    def get_environment() -> str:
        return settings.ENVIRONMENT

    @staticmethod
    def get_version() -> str:
        return settings.VERSION
