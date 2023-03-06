import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Parent configuration class."""

    DEBUG = False
    CSRF_ENABLED = True
    AUTHENTIFICATION_SERVICE = os.getenv("APIREST_AUTHENTIFICATION_SERVICE")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Configurations for Development."""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("APIREST_DB") or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""

    TESTING = True
    DEBUG = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = os.getenv("APIREST_TEST_DB")


class StagingConfig(Config):
    """Configurations for Staging."""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("APIREST_DB")


class ProductionConfig(Config):
    """Configurations for Production."""

    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("APIREST_PRODUCTION_DB")


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
}

