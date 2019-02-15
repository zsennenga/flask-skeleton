from config.config_base import ConfigBase


class Config(ConfigBase):
    DB_DRIVER = 'sqlite'
    DB_HOST = ''
    DB_DATABASE = 'dev'
    DB_USER = ''
    DB_PASS = ''

    SECRET_KEY = 'buts lol'

    SERVER_NAME = None
