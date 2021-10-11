# -*- coding: utf-8 -*-
"""Application configuration."""
from os import path

class Config(object):
    SECRET_KEY = os.enrion.get('SECRET_KEY')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    SERVER_IP = '10.5.40.10'
    API_VESION = ""


class ProductionConfig(Config):
    ENV = "Production"
    DB_NAME = 'development.db'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'.join(path.join(SERVER_IP, DB_NAME))
    CACHE_TYPE = 'simple'

class DevelopmentConfig(Config):
    ENV = "Development"
    DEBUG = True
    DB_NAME = 'development.db'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'.join(path.join(SERVER_IP, DB_NAME))
    CACHE_TYPE = 'simple'

class TestConfig(Config):
    ENV = "Test"
    DB_NAME = 'test.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///:memory:'
    CACHE_TYPE = 'simple'
    BCRYPT_LOG_ROUNDS = 4
