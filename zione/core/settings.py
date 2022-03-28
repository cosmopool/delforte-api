# -*- coding: utf-8 -*-
"""Application configuration."""
import logging
import os
from datetime import timedelta


class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get("SECRET_KEY")
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.

    # jwt
    JWT_AUTH_USERNAME_KEY = "username"
    # JWT_AUTH_HEADER_PREFIX = 'Token'
    # JWT_HEADER_TYPE = 'Token'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(10**6)

    # log
    LOG_LEVEL = logging.ERROR

    # database
    HOST = os.environ["DATABASE_HOST"]
    PORT = os.environ["DATABASE_PORT"]
    USER = os.environ["DATABASE_USER"]
    PASSWORD = os.environ["DATABASE_PASS"]
    DB_NAME = os.environ["DATABASE_NAME"]
    CONNECTION = (
        f"host={HOST} port={PORT} user={USER} password={PASSWORD} dbname={DB_NAME}"
    )


class ProdConfig(Config):
    """Production configuration."""

    ENV = "production"
    DEBUG = False


class DevConfig(Config):
    """Development configuration."""

    ENV = "development"
    DEBUG = True
    DB_NAME = "development"
    CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.
    JWT_ACCESS_TOKEN_EXPIRES = False
    HOST = "0.0.0.0"
    PORT = "5432"
    USER = "zione"
    PASSWORD = "test_pass"
    DB_NAME = "test"
    CONNECTION = (
        f"host={HOST} port={PORT} user={USER} password={PASSWORD} dbname={DB_NAME}"
    )

    # log
    LOG_LEVEL = logging.DEBUG
    SSL_CONTEXT = True


class TestConfig(Config):
    """Test configuration."""

    ENV = "testing"
    TESTING = True
    DEBUG = True
    JWT_ACCESS_TOKEN_EXPIRES = False
    HOST = "0.0.0.0"
    PORT = "5432"
    USER = "zione"
    PASSWORD = "test_pass"
    DB_NAME = "test"
    CONNECTION = (
        f"host={HOST} port={PORT} user={USER} password={PASSWORD} dbname={DB_NAME}"
    )

    # log
    LOG_LEVEL = logging.DEBUG
