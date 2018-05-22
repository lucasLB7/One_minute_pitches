import os


class Config:

    SECRET_KEY = 'AbeautifulSecretKey'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://d4rkkn1t3:Dedecocomagna1@localhost/pitches'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class TestConfig(Config):
    pass


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True



config_options = {
    'development': DevConfig,
    'production' : ProdConfig,
    'test' : TestConfig
}