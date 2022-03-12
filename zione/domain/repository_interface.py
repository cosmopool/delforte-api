from abc import ABC, abstractmethod
from dataclasses import dataclass

from zione.domain.entities.response import Response


@dataclass
class RepositoryInterface(ABC):
    """Interface for all repositories classes"""

    connection: str

    @abstractmethod
    def insert(self, entry: dict[str, str], table: str) -> Response:
        """Add an entry to the database"""

    @abstractmethod
    def delete(self, id: int, table: str) -> Response:
        """Remove an entry from the database"""

    @abstractmethod
    def update(self, entry: dict[str, str], table: str, id: int = -1) -> Response:
        """Edit an entry in the database"""

    @abstractmethod
    def select(self, entry: dict[str, str], table: str) -> Response:
        """Fetch an entry from the database"""

    @abstractmethod
    def insert_user(self, entry: dict[str, str]) -> Response:
        """Fetch an entry from the database"""

    @abstractmethod
    def auth_user(self, entry: dict[str, str]) -> Response:
        """Fetch an entry from the database"""
