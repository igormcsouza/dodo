from os import getenv


class Config(object):
    """Main config object"""
    FLASK_ENV = getenv("FLASK_ENV", "development")
    SECRET_KEY = getenv("SECRET_KEY", "mysupersecretkey")


class DevelopmentConfig(Config):
    """Development config"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL", "sqlite:///dodo.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """Testing config"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = getenv("TEST_DATABASE_URL",
                                     "sqlite:///dodo_test.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Production config"""
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL", "sqlite:///dodo.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
