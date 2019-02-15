class ConfigBase:
    DB_DRIVER = ''
    DB_HOST = ''
    DB_DATABASE = ''
    DB_USER = ''
    DB_PASS = ''

    SECRET_KEY = None

    SERVER_NAME = None

    @classmethod
    def db_uri(cls):
        if cls.DB_DRIVER == 'mysql':
            return 'mysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_DATABASE}'.format(
                DB_USER=cls.DB_USER,
                DB_PASS=cls.DB_PASS,
                DB_HOST=cls.DB_HOST,
                DB_DATABASE=cls.DB_DATABASE,
            )
        elif cls.DB_DRIVER == 'sqlite':
            return 'sqlite:////tmp/{}'.format(
                cls.DB_DATABASE,
            )
        else:
            raise Exception('Invalid DB Driver: {}'.format(
                cls.DB_DRIVER
            ))
