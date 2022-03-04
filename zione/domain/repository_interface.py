from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from zione.core.settings import CONNECTION
from zione.domain.entities.response import Response

@dataclass
class RepositoryInterface(ABC):
    """Interface for all repositories classes"""

    connection: str = CONNECTION

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









# @dataclass
# class RepositoryInterface(ABC):
#     """Interface for all repositories classes"""
#
#     @abstractmethod
#     def add(self, entry, endpoint: str) -> int:
#         """Add an entry to the database"""
#
#     @abstractmethod
#     def remove(self, entry, endpoint: str) -> int:
#         """Remove an entry from the database"""
#
#     @abstractmethod
#     def edit(self, entry, endpoint: str) -> int:
#         """Edit an entry in the database"""
#
#     @abstractmethod
#     def fetch(self, entry, endpoint: str) -> dict:
#         """Fetch an entry from the database"""
