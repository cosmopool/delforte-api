import logging
from psycopg import connect

from zione.core.enums import Status
from zione.core.exceptions import DatabaseError, MissingFieldError
from zione.domain.entities.response import Response
from zione.domain.repository_interface import RepositoryInterface


# @dataclass
class PostgresRepository(RepositoryInterface):
    """Interface for all datasources classes"""

    def _make_update_str(self, record):
        keys = record.keys()
        list = []

        for key in keys:
            list.append(f"\"{ key }\" = '{ record.get(key) }'")

        return ", ".join(list)

    def _return_command_status(self, byte):
        byte_to_str = "".join(map(chr, byte))
        status_list = byte_to_str.rsplit(" ")
        status = status_list[len(status_list) - 1]

        return int(status)

    def _str_values(self, tuple):
        """Print a string with `%s` for each element of a tuple. Usable for a psycopg SQL query."""
        result = []
        for _ in tuple:
            result.append("%s")
        result = ", ".join(result)

        return result

    def _query_vals(self, entry: dict[str, str]) -> tuple[str, str]:
        """Return entry keys and values as columns and values in string form separated by comma, to be used in a query."""
        columns = []
        values = []

        for val in entry.values():
            values.append(f"'{val}'")

        for col in entry.keys():
            columns.append(f'"{col}"')

        columns = ", ".join(columns)
        values = ", ".join(values)

        return columns, values

    def _insert(self, query: str) -> Response:
        logging.debug(f"Query used: {query}")

        try:
            with connect(self.connection) as conn:
                query_result = conn.execute(query).fetchall()
                res = query_result[0][0]["id"]

                logging.debug(f"Result from db: {query_result}")
                logging.debug(f"Result sent as response: {res}")

                return Response(status=Status.Success, result=[res], http_code=200)

        except Exception as e:
            logging.error(e)
            err_msg = e.__str__()

            return Response(
                status=Status.Error,
                error=DatabaseError("Error on insert"),
                message=err_msg,
                http_code=500,
            )

    def insert(self, record: dict, table: str) -> Response:
        """Add an record to the database"""

        table = f"{table}_view"
        columns, values = self._query_vals(record)

        query = f"WITH entry AS (INSERT INTO {table} ({columns}) VALUES ({values}) RETURNING id) SELECT row_to_json(entry) FROM entry"

        return self._insert(query)

    def delete(self, id: int, table: str) -> Response:
        """Remove an record from the database"""

        query = f"DELETE FROM { table } WHERE id = { id }"
        logging.debug(f"Query used: {query}")

        try:
            with connect(self.connection) as conn:
                query_result = conn.execute(query).pgresult.command_status
                res = self._return_command_status(query_result)

                logging.debug(f"Result from db: {query_result}")
                logging.debug(f"Result sent as response: {res}")

                return Response(status=Status.Success, result=[res], http_code=200)

        except Exception as e:
            logging.error(e)
            err_msg = e.__str__()

            return Response(
                status=Status.Error,
                error=DatabaseError("Error on delete"),
                message=err_msg,
                http_code=500,
            )

    def update(self, record: dict, table: str, id: int = -1) -> Response:
        """Edit an record in the database"""

        table = f"{table}_view"
        if id < 0:
            id = record.get("id")

        if record.get("id", None):
            record.pop("id")

        query = (
            f"UPDATE { table } SET { self._make_update_str(record) } WHERE id = { id }"
        )
        logging.debug(f"Query used: {query}")

        try:
            with connect(self.connection) as conn:
                query_result = conn.execute(query)
                status = self._return_command_status(
                    query_result.pgresult.command_status
                )

                logging.debug(f"Result from db: {query_result}")
                logging.debug(f"Result sent as response: {status}")

                return Response(status=Status.Success, result=[status], http_code=200)

        except Exception as e:
            logging.error(e)
            err_msg = e.__str__()

            return Response(
                status=Status.Error,
                error=DatabaseError("Error on update"),
                message=err_msg,
                http_code=500,
            )

    def select(self, record: dict, table: str):
        table = f"{table}_view"

        if len(record.keys()) > 0:
            column = "".join(record.keys())
            value = "".join(record.values())
            query = f'SELECT row_to_json({ table }) FROM { table } WHERE "{ column }" { value }'
        else:
            query = f"SELECT row_to_json({table}) FROM {table}"

        return self._select(record, query)

    def _select(self, record: dict, query: str):
        """Fetch an record from the database"""
        res = []
        logging.debug(f"Query used: {query}")

        try:
            with connect(self.connection) as conn:
                query_result = conn.execute(query).fetchall()
                for record in query_result:
                    if record is not None:
                        res.append(record[0])

                if len(res) == 0:
                    raise KeyError(" No record found with given id.")

                logging.debug(f"Result from db: {query_result}")
                logging.debug(f"Result sent as response: {res}")

                return Response(status=Status.Success, result=res, http_code=200)

        except Exception as e:
            logging.error(e)
            err_msg = e.__str__()

            return Response(
                status=Status.Error,
                error=DatabaseError("Error on select"),
                message=err_msg,
                http_code=500,
            )

    def _insert_user(self, query: str) -> Response:
        logging.debug(f"Query used: {query}")

        try:
            with connect(self.connection) as conn:
                query_result = conn.execute(query).pgresult.command_status

                res = self._return_command_status(query_result)

                logging.debug(f"Result from db: {query_result}")
                logging.debug(f"Result sent as response: {res}")

                return Response(status=Status.Success, result=[res], http_code=200)

        except Exception as e:
            logging.error(e)
            err_msg = e.__str__()

            return Response(
                status=Status.Error,
                error=DatabaseError("Error on insert"),
                message=err_msg,
                http_code=500,
            )

    def insert_user(self, record: dict) -> Response:
        username = record.get("username", None)
        password = record.get("password", None)

        if username and password:
            query = f"INSERT INTO users (username, password) VALUES ('{ username }', crypt('{ password }', gen_salt('bf')))"

            return self._insert_user(query)

        else:
            return Response(
                status=Status.Error,
                error=MissingFieldError(),
                message="Field username and password is required",
                http_code=500,
            )

    def auth_user(self, record: dict):
        """Return a recordionaries of records"""
        username = record.get("username")
        password = record.get("password")

        if username and password:
            query = f"SELECT row_to_json(users) FROM users WHERE username = '{ username }' AND password = crypt('{ password }', password)"
            return self._select(record, query)
        else:
            return Response(
                status=Status.Error,
                # TODO: use other error. eg. AuthError
                error=MissingFieldError(),
                message="Field username and password is required",
                http_code=500,
            )
