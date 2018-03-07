class SecretKeyName:
    # static member
    ENVIRONMENT = 'environment'

    SECRET_KEY = 'secret_key'

    MEMCACHED_LOCATION = 'memcached_location'

    DEFAULT_DB_HOST = 'default_db_host'
    DEFAULT_DB_PORT = 'default_db_port'
    DEFAULT_DB_ACCOUNT = 'default_db_account'
    DEFAULT_DB_PASSWORD = 'default_db_password'

    SENTRY_DSN = 'sentry_dsn'

    NAVER_OPEN_API_CLIENT_ID = 'naver_open_api_client_id'
    NAVER_OPEN_API_CLIENT_SECRET = 'naver_open_api_client_secret'


class Environment:
    DEV = 'development'
    PROD = 'production'
