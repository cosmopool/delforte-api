from flask import Flask

from zione.infra.repositories.postgres_repository import PostgresRepository


def make_repository(app: Flask, repository=PostgresRepository):
    """Return repository instance with a connection string from app configuration object"""
    return repository(app.config["CONNECTION"])
