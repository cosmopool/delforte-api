from zione.core.settings import CONNECTION
from zione.infra.repositories.postgres_repository import PostgresRepository

REPOSITORY = PostgresRepository(CONNECTION)
